from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['frontpage.fyi']

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["post", repo, rkey]:
            return at_url(repo, "fyi.unravel.frontpage.post", rkey)
        case ["post", _, _, repo, rkey]:
            return at_url(repo, "fyi.unravel.frontpage.comment", rkey)
        case ["profile", repo]:
            return at_url(repo)
    return None

# TODO frontpage should add in URLs for posts/comments like reddit has. for now it has profile URLs but not collection-specific ones.
