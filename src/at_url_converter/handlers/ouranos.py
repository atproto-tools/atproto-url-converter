from at_url_converter.atproto_utils import get_did, url_obj, at_url
from at_url_converter.boilerplate import get_index
from at_url_converter import lex

# source https://github.com/pdelfan/ouranos/tree/main/src/app (subfolders are routes)
hosts = ["useouranos.app"]

async def handler(u: url_obj):
    if uri := u.find_query_param("uri"):
        return at_url.from_str(uri)
    match get_index(u.path, 1):
        case "user":
            if did := await get_did(u.path[2]):
                if get_index(u.path, 3) == "post":
                    return at_url(did, lex.bsky.post, u.path[4])
                return at_url(did, lex.bsky.profile, "self")
