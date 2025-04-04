from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['pinboards.jeroba.xyz']

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["profile", repo, "board", rkey]:
            return at_url(repo, "xyz.jeroba.tags.tag", rkey)
    return None
