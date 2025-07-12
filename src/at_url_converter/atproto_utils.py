from collections.abc import AsyncGenerator
import os
from typing import Annotated, Any, ClassVar, Literal, Optional, cast
from pydantic import BaseModel, BeforeValidator, model_validator
from at_url_converter.boilerplate import get_index, get_timed_logger
import re
from atproto import AsyncIdResolver, AsyncDidInMemoryCache, AsyncClient
from atproto.exceptions import AtProtocolError
from atproto_client.models.com.atproto.repo.list_records import Params, Record
# TODO consider switching to a different parsing lib for better validation https://sethmlarson.dev/why-urls-are-hard-path-params-urlparse
from urllib.parse import urlparse, parse_qsl, unquote, urlunparse
from atproto_client.models.string_formats import Did, AtIdentifier, Nsid, RecordKey
from atproto_client.models.string_formats import Handle as _Handle

Handle = Annotated[_Handle, BeforeValidator(lambda x: x.removeprefix("@") if isinstance(x, str) else x)]

VALIDATE_AT_URL_FIELDS = os.environ.get("AT_URL_CONVERTER_VALIDATE_AT_URL_FIELDS", "0") # s1 to enable globally, 0 or unset to disable

log = get_timed_logger("converter")

MAX_LIST_LIMIT = 100
MAX_BATCH_SIZE = 100 # batch size 100 defined by https://docs.bsky.app/docs/api/com-atproto-repo-list-records

#TODO ok this is technically incorrect, it ignores trailing slashes
def split_path(path_str: str, remove_trailing = True) -> list[str]:
    path_str = path_str.removeprefix("/")
    if remove_trailing:
        path_str = path_str.removesuffix("/")
    if not path_str:
        return []
    return [unquote(i) for i in path_str.split("/")]

def path_index(path: list[str] | str, index: int, default: Optional[str] = None):
    if isinstance(path, str):
        path = split_path(path)
    return get_index(path, index, default)

type parsed_query = list[tuple[str, str]]
def parse_query(query_str: str) -> parsed_query:
    return [(unquote(k), unquote(v)) for k, v in parse_qsl(query_str)]


type query_or_str = str | parsed_query
def parse_query_str(data: query_or_str) -> parsed_query:
    if isinstance(data, str):
        return parse_query(data)
    else:
        return data

def find_query_param(param: str, query: query_or_str, ensure_unique = True) -> str | None:
    query = parse_query_str(query)
    found = [p[1] for p in query if p[0] == param]
    if len(found) > 1:
        error_msg = f"multiple values for {param} in query {query}:\n{found}"
        if ensure_unique:
            raise ValueError(error_msg)
        else:
            log.error(error_msg)
    return found[0] if found else None

class url_obj:
    def __init__(self, url: str):
        parsed = urlparse(url)
        self.og_parsed = parsed
        self.og = url
        
        self.scheme = parsed.scheme
        self.netloc = parsed.netloc
        self.path = split_path(parsed.path)
        self.params = parsed.params # the red-headed stepchild of urlparse :(
        self.query = parse_query(parsed.query)
        self.fragment = parsed.fragment
        
    @staticmethod
    def split_path(path_str: str):
        return split_path(path_str)

    @staticmethod
    def parse_query(query_str: str):
        return parse_query(query_str)

    def path_index(self, index: int, default: Optional[str] = None, path: Optional[list[str] | str] = None):
        if path is None:
            path = self.path
        return path_index(path, index, default)

    def find_query_param(self, param: str, query: Optional[str | list[tuple[str, str]]] = None) -> str | None:
        if query is None:
            query = self.query
        return find_query_param(param, query)

type AllowEmpty[T] = T | Literal[""]

class at_url(BaseModel):
    """object that stores components of an at URI. parts acessible by dot notation"""
    did: AllowEmpty[Did]= ""
    collection: AllowEmpty[Nsid] = ""
    rkey: AllowEmpty[RecordKey] = ""
    query: Annotated[parsed_query, BeforeValidator(parse_query_str)] = []
    fragment: str = ""
    handle: AllowEmpty[Handle] = ""

    strict_string_flag: ClassVar[bool] = bool(int(VALIDATE_AT_URL_FIELDS))

    def __init__(
        self,
        repo: Optional[AtIdentifier] = None,
        collection: Optional[Nsid] = None,
        rkey: Optional[RecordKey] = None,
        query: Optional[str | list[tuple[str, str]]] = None,
        fragment: Optional[str] = None,
        *,
        did: Optional[Did] = None,
        handle: Optional[Handle] = None,
        strict_string_flag: Optional[bool] = None
    ):
        out = {
            "did": did or "",
            "handle": handle or "",
            "collection": collection or "",
            "rkey": rkey or "",
            "query": query or [],
            "fragment": fragment or "",
        }
        if repo:
            if repo.startswith("did:"):
                if did:
                    log.warning(f"make_at_url: did {did} is being replaced by repo {repo}")
                out["did"] = repo
            else:
                if handle:
                    log.warning(f"make_at_url: handle {handle} is being replaced by repo {repo}")
                out["handle"] = repo

        if strict_string_flag is None:
            strict_string_flag = at_url.strict_string_flag
        self.__pydantic_validator__.validate_python(out, self_instance=self, context={"strict_string_format": strict_string_flag})

    @model_validator(mode="after")
    def _check_repo(self):
        if not (self.handle or self.did):
            raise ValueError("at_url: either 'handle' or 'did' must be present")
        return self

    @classmethod
    def from_str(cls, url: str):
        # the spec said we could use urlparse, so we do ^_^ technically aturls are not valid urls tho
        # https://github.com/bluesky-social/atproto-website/issues/417
        parsed = urlparse(url)
        path = split_path(parsed.path)
        if len(path) > 2:
            raise ValueError(f"excessively long path path in atproto url:\n{url}\n{path}")
        return cls(
            parsed.netloc,
            path[0],
            path[1],
            parsed.query,
            parsed.fragment
        )


    @property
    def repo(self) -> AtIdentifier:
        repo = self.did or self.handle
        if not repo:
            raise AttributeError(f"at_url {repr(self)} has no defined repo")
        return repo

    def __repr__(self):
        set_fields = {k: v for k,v in self.__repr_args__() if k and v} # idk why __repr_args__() returns None for some keys
        args = ", ".join([k + "=" + (str(v) if k == "query" else f"'{v}'") for k,v in set_fields.items()])
        return f'{self.__class__.__name__}({args})'

    async def get_handle(self, verify: Literal[0, 1, 2] = 0):
        '''
        gets a handle, potentially looking it up (1 request)

        Args:
            verify (Literal[0, 1, 2], optional): 0 takes the source at its word, if handle is present, but resolves the did if not. (0 or 1 request)\n
                1 makes a request to see if the handle points to DID. (1 or 2 requests)\n
                2 resolves handle, fetches did doc, checks if handle matches did. if not, attempts to verify new handle and return that. (up to 3 requests)\n
                Defaults to 0.

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        '''        
        try:
            if self.handle:
                if verify == 0:
                    return self.handle

                did = await resolver.handle.ensure_resolve(self.handle)
                if self.did and self.did != did: # should rarely happen, usually we have one or the other in a url
                    log.warning(f"replacing self's did {self.did} with fetched {did}")
                self.did = did
                
                if verify == 1:
                    return self.handle

            elif self.did:
                if verify < 2:
                    return await get_handle(self.did)
                doc_handle, valid = await check_did_handle(cast(str, self.did))
                if doc_handle and valid:
                    if self.handle != doc_handle:
                        log.info(f"replacing self's handle {self.handle} with {doc_handle}")
                        self.handle = doc_handle
                elif doc_handle and not valid:
                    # TODO should probably do something more significant that warning. alternate return val?
                    log.warning(f"found new handle {doc_handle} but could not verify")
                    return None
                return doc_handle
            else:
                raise AttributeError(f"at_url {self} has no did or handle")
        except AtProtocolError as e:
            log.error(e)
            return None

    async def get_did(self, verify: Literal[0, 1, 2] = 0) -> AtIdentifier | None: #TODO add validation after fetch
        """
        Asynchronously retrieves and verifies the Decentralized Identifier (DID) associated with the current instance.

        Args:
            verify (Literal[0, 1, 2], optional): 
                Verification level for the DID and handle.
                - 0: No verification, return cached DID if available.
                - 1: Verify the DID by resolving it.
                - 2: Additionally verify that the handle matches the DID document.

        Returns:
            Optional[AtIdentifier]: The resolved and optionally verified DID, or None if resolution fails.

        Raises:
            AttributeError: If neither DID nor handle is available for resolution.
            ValueError: If the resolved DID does not match the expected value.

        Notes:
            - If both DID and handle are present, the method ensures they are consistent.
            - If only the handle is present, it attempts to resolve the DID from the handle.
            - Logs warnings if inconsistencies are found or if verification fails.
            - Returns None and logs an error if an AtProtocolError is encountered during resolution.
        """
        try:
            if self.did:
                if not verify:
                    return self.did
                doc = await resolver.did.ensure_resolve(self.did)
                did = doc.get_did()
                if self.did != did:
                    raise ValueError(f"self's did {self.did} did not match doc's did {did}")
            elif self.handle:
                did = await resolver.handle.ensure_resolve(self.handle)
                if self.did and self.did != did: # should rarely happen, usually we have one or the other in a url
                    log.warning(f"replacing self's did {self.did} with fetched {did}")
                self.did = did
                if verify < 2:
                    return self.did
                doc_handle, valid = await check_did_handle(self.did)
                if doc_handle and valid:
                    if self.handle != doc_handle:
                        log.info(f"replacing self's handle {self.handle} with {doc_handle}")
                    self.handle = doc_handle
                elif doc_handle and not valid:
                    # TODO should probably do something more significant that warning. alternate return val?
                    log.warning(f"found alternate handle {doc_handle} but could not could not verify it")
            else:
                raise AttributeError(f"at_url {self} has no did or handle")
            return self.did
        except AtProtocolError as e:
            log.error(e)
            return None

    async def get_pds(self, verify: Literal[0, 1] = 0):
        if did := await self.get_did():
            return await get_pds(did, verify)

    def __str__(self):
        cs = self.collection
        rs = self.rkey
        ps = cs + "/" + rs if rs else cs
        ql = getattr(self, "query", [])
        qs = "&".join("=".join((i[0], i[1])) for i in ql) if self.query else "" # using .join() because not all queries have params
        return urlunparse(("at", self.repo, ps, "", qs, self.fragment or ""))

# afaict these use a single global client so we should be good to loop
resolver = AsyncIdResolver(cache=AsyncDidInMemoryCache())
c = AsyncClient()
_get_record = c.com.atproto.repo.get_record
_describe_repo = c.com.atproto.repo.describe_repo
httpx_client = c._request._client #TODO ask is this bad? i don't really want to make my own client if i can steal one tbh

async def get_record(u: at_url):
    c.update_base_url(await u.get_pds())
    if not u.collection or not u.rkey:
        raise ValueError(f"get_record: {u} is not a link to a record")
    return await _get_record({
        "repo": u.repo,
        "collection": u.collection,
        "rkey": u.rkey
    })

async def get_handle(did: str):
    try:
        doc = await resolver.did.ensure_resolve(did)
        return doc.get_handle()
    except AtProtocolError as e:
        log.warning(e)

async def check_did_handle(did: str) -> tuple[str | None, bool]:
    try:
        if handle := await get_handle(did):
            valid = did == await resolver.handle.ensure_resolve(handle)
            return handle, valid
        else:
            return None, False
    except AtProtocolError as e:
        log.warning(e)
        return None, False

async def get_pds(identifier: str, verify: Literal[0, 1] = 0):
    if did := await get_did(identifier):
        if doc := await resolver.did.resolve(did):
            if endpoint := doc.get_pds_endpoint():
                if not verify:
                    return endpoint

                if _describe_repo({"repo": endpoint}):
                    #longterm maybe validate the response before returning idk
                    return endpoint
                else:
                    return None
        else:
            log.error(f"could not get pds for {did}")

_handle_segment = r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)"
handle_pattern = re.compile(r"^(?:segment\.)+segment$".replace("segment", _handle_segment))
did_pattern = re.compile(r"^did:(?P<method>[a-z0-9]+):(?P<identifier>(?:(?:[a-zA-Z0-9._-]|%[a-fA-F0-9]{2})*:)*(?:[a-zA-Z0-9._-]+|%[a-fA-F0-9]{2})+)$")

async def get_did(repo: str | None, verify: Literal[0, 1, 2] = 0):
    if not repo:
        return None

    if did_pattern.match(repo) and not verify:
        return repo
    elif handle_pattern.match(repo):
        log.debug(f"resolving handle {repo}")
        repo = await resolver.handle.resolve(repo)
        if not verify:
            return repo
    else:
        log.error(f"Invalid repo {repo}")
        return None

    if repo:
        log.debug(f"resolving did {repo}")
        if doc := await resolver.did.resolve(repo):
            doc_did = doc.get_did()
            if doc_did != repo:
                log.warning(f"did in doc {doc_did} does not match requested did {repo}")
            return repo

    return None

async def list_records(u: at_url, limit: int | Literal[False] = MAX_LIST_LIMIT, batch_size: int = MAX_BATCH_SIZE) -> AsyncGenerator[Record, Any]:
    
    c.update_base_url(await get_pds(u.repo))
    if isinstance(limit, int) and limit < 1:
        raise ValueError("limit must be positive")
    if limit and limit < batch_size:
        batch_size = limit
    p = Params(
        collection=u.collection,
        repo=u.repo,
        limit=batch_size
    )
    while limit is False or limit > 0:
        #TODO maybe add an eager fetch that immediately fetches the next batch again
        r = await c.com.atproto.repo.list_records(p)

        for rec in r.records:
            yield rec

        if limit:
            limit -= len(r.records)
            p.limit = min(batch_size, limit)

        if not r.cursor or (limit and limit <= 0):
            return
        else:
            p.cursor = r.cursor

async def find_record(u: at_url, match_dict: dict[str, Any], limit: int | Literal[False] = MAX_LIST_LIMIT, batch_size: int = MAX_BATCH_SIZE) -> Record | None:
    rec_list = list_records(u, limit, batch_size)
    async for rec in rec_list:
        # un-import-able atproto_client.models.dot_dict - not actually dict, but a model that contains a dict and allows dot notation
        rec_value: dict[str, Any] = cast(dict, rec.value)
        if match_dict.keys() <= rec_value.keys(): # dict.keys() can do everything in collections.abc.Set
            if all(rec_value[k] == v for k,v in match_dict.items()):
                await rec_list.aclose()
                return rec
