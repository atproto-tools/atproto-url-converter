from at_url_converter.atproto_utils import get_index, get_did, url_obj, at_url
from at_url_converter import lex

# source: routes that include the substring '/:did' in https://github.com/mary-ext/aglais/blob/trunk/src/routes.ts
# list of hostnames that potentially match this handler

hosts: list[str] = ['aglais.pages.dev']

async def handler(u: url_obj) -> at_url | None:
    if did := await get_did(u.path[0]):
        out = at_url(did)
        match get_index(u.path, 1):
            case "curation-lists" | "moderation-lists" | "lists":
                out.collection = lex.bsky.list
                if rkey := get_index(u.path, 2):
                        out.rkey = rkey
            case "following":
                out.collection = lex.bsky.follow
            case "feeds":
                out.collection = lex.bsky.feedgen
                if rkey := get_index(u.path, 2):
                    out.rkey = rkey
            case "likes":
                out.collection = lex.bsky.like
            case rkey if isinstance(rkey, str):
                out.collection, out.rkey = lex.bsky.post, rkey
            case None:
                out.collection, out.rkey = lex.bsky.profile, "self"
        return out
