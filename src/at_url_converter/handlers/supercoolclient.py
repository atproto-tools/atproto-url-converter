from at_url_converter.atproto_utils import url_obj, at_url
from at_url_converter import lex

hosts = ['supercoolclient.pages.dev']

async def handler(u: url_obj) -> at_url | None:
    if repo := u.path_index(0):
        out = at_url(repo)
        match u.path[1:]:
            case ["post", rkey]:
                out.collection, out.rkey = lex.bsky.post, rkey
        return out
        
