from at_url_converter.atproto_utils import get_index, url_obj, at_url
from at_url_converter import lex

hosts = ['clearsky.app']

async def handler(u: url_obj) -> at_url | None:
    if did := get_index(u.path, 0):
        out = at_url(did)
        match u.path_index(1):
            case "blocking":
                out.collection = lex.bsky.block
            case "history" | None:
                out.collection = lex.bsky.post
            case "packs":
                out.collection = lex.bsky.starterpack
        return out
    return None
