# ruff: noqa: F401
from collections.abc import AsyncGenerator, Sequence
from typing import Any, Literal, Optional, cast
from at_url_converter.boilerplate import get_index, get_timed_logger
import re
from atproto import AsyncIdResolver, AsyncDidInMemoryCache, AsyncClient
from atproto.exceptions import AtProtocolError
from atproto_client.models.com.atproto.repo.get_record import Response
from atproto_client.models.com.atproto.repo.list_records import Params, Record
# TODO consider switching to a different parsing lib for better validation https://sethmlarson.dev/why-urls-are-hard-path-params-urlparse
from collections.abc import Mapping
from urllib.parse import urlparse, parse_qsl, unquote, urlunparse
from atproto_client.models.string_formats import AtIdentifier, Nsid, RecordKey
log = get_timed_logger("converter")

MAX_LIST_LIMIT = 100
MAX_BATCH_SIZE = 100 # batch size 100 defined by https://docs.bsky.app/docs/api/com-atproto-repo-list-records

def split_path(path_str: str) -> list[str]:
    return [unquote(i) for i in path_str.split("/") if i]

def path_index(path: list[str] | str, index: int, default: Optional[str] = None):
    if isinstance(path, str):
        path = split_path(path)
    return get_index(path, index, default)

def parse_query(query_str: str) -> list[tuple[str, str]]:
    return [(unquote(k), unquote(v)) for k, v in parse_qsl(query_str)]

def find_query_param(param: str, query: str | list[tuple[str, str]]) -> str | None:
    if isinstance(query, str):
        query = parse_query(query)
    found = [p[1] for p in query if p[0] == param]
    if len(found) > 1:
        log.error(f"found multiple values for param {param} in query {query}:\n{found}")
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

#TODO this should really be a pydantic model but that needs coordination. ask marshalx for pointers/approval
class at_url(Mapping):
    """object that stores components of an at URI. parts acessible by dot notation"""
    did: str | None
    handle: str | None
    # @validate_call(config={"strict": True})
    def __init__(
        self,
        # repo: AtIdentifier,
        # collection: Nsid = None,
        # rkey: RecordKey = None,
        repo: str,
        collection: Optional[str] = None,
        rkey: Optional[str] = None,
        # cid: Optional[str] = None,
        query: Optional[str | Sequence[tuple[str, str]]] = None,
        fragment: Optional[str] = None,
        handle: Optional[str] = None
    ):
        """handle is an optional param in case you want to store both for some reason. stringify-ing the uri will always output the DID"""
        if not repo:
            raise ValueError(f'no valid repo in at_url constructor! args: {locals()}')
        repo = repo.removeprefix("@")
        if did_pattern.match(repo):
            self.did, self.handle = repo, handle or ""
        elif handle_pattern.match(repo):
            self.handle, self.did = repo, ""
        else:
            raise ValueError(f"repo param {repo} is not a handle or did!")
        
        self.collection: Nsid = collection or ""
        self.rkey: RecordKey = rkey or ""
        # self.cid: Cid = cid or ""
        if isinstance(query, str):
            self.query = parse_query(query or "")
        else:
            self.query = list(query) if query else []
        self.fragment = fragment or ""

    parts = ("repo", "collection", "rkey", "query", "fragment")

    @classmethod
    def from_str(cls, url: str):
        #TODO add proper validation function from atproto_client.models.string_formats
        parsed = urlparse(url)
        repo = parsed.netloc
        path = split_path(parsed.path)
        if len(path) > 2:
            raise ValueError(f"at_url.from_str(): excessively long path path in atproto url:\n{url}\n{path}")
        collection = get_index(path, 0)
        rkey = get_index(path, 1)
        query = parsed.query
        fragment = parsed.fragment
        return cls(repo, collection, rkey, query, fragment)

    @property
    def repo(self) -> AtIdentifier:
        repo = self.did or self.handle
        if not repo:
            placeholder_repr = {k: self[k] for k in self.parts[1:]}
            #TODO convert to pydantic model so repr looks decent
            raise AttributeError(f"at_url {placeholder_repr} has no defined repo")
        return repo

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
    
    def __iter__(self):
        yield from self._get_parts()

    def __getitem__(self, key: str):
        if key in at_url.parts:
            return getattr(self, key)
        else:
            raise KeyError(f"{key} is not a valid part of an at_url")
        
    def __len__(self):
        return len(self._get_parts())

    def _get_parts(self):
        return {part: part_val for part in at_url.parts if (part_val := getattr(self, part, None))}
        # return tuple(part_val for part in at_url.parts if (part_val := getattr(self, part)))

    def __eq__(self, value) -> bool:
        if isinstance(value, at_url):
            return self._get_parts() == value._get_parts()
        else:
            return False

    def __str__(self):
        cs = self.collection
        rs = self.rkey
        ps = cs + "/" + rs if rs else cs
        ql = getattr(self, "query", [])
        qs = "&".join("=".join((i[0], i[1])) for i in ql) if self.query else ""
        try:
            repo = self.repo
        except ValueError:
            repo = "<missing repo>"
        return urlunparse(("at", repo, ps, "", qs, self.fragment or ""))

    def __repr__(self):
        parts = self._get_parts()
        if self.did and self.handle:
            parts['handle'] = self.handle
        args = ", ".join([k + "=" + (str(v) if k == "query" else f"'{v}'") for k,v in parts.items()])
        return f"at_url({args})"

# afaict these use a single global client so we should be good to loop
resolver = AsyncIdResolver(cache=AsyncDidInMemoryCache())
c = AsyncClient()
_get_record = c.com.atproto.repo.get_record
_list_records = c.com.atproto.repo.list_records
_describe_repo = c.com.atproto.repo.describe_repo
httpx_client = c._request._client #TODO ask is this bad? i don't really want to make my own client if i can steal one tbh

async def get_record(u: at_url) -> Response:
    c.update_base_url(await get_pds(u.repo))
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
        r = await _list_records(p)

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
