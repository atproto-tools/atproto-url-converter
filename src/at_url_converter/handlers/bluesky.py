from at_url_converter.atproto_utils import get_index, log, url_obj, at_url
from at_url_converter.lex import bsky

hosts = ["bsky.app", "main.bsky.dev", "langit.pages.dev", "tokimekibluesky.vercel.app"]
async def handler(u: url_obj) -> at_url | None:
    if u.netloc ==  "langit.pages.dev":
        match u.path:
            case ["u", _, *rpath]:
                u.path = rpath
            case _:
                return None
    did = u.path_index(1)
    if not did:
        return None

    match u.path_index(0):
        case "starter-pack":
            return at_url(did, bsky.starterpack, u.path[2])
        case "profile":
            if rkey := get_index(u.path, 3):
                match u.path[2]:
                    case "post":
                        return at_url(did, bsky.post, rkey)
                    case "feed":
                        return at_url(did, bsky.feedgen, rkey)
                    case "lists":
                        return at_url(did, bsky.list, rkey)
                    case "follows":
                        return at_url(did, bsky.follow)
                    case _:
                        log.error(f"uknown suffix {u.path[2]} in {u.og}")
            else:
                return at_url(did, bsky.profile, "self")
