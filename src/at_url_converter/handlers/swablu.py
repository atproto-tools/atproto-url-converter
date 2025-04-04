from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['swablu.pages.dev']

async def handler(u: url_obj) -> at_url | None:
    path = u.split_path(u.fragment)
    match path:
        case ["list" | "post", uri]:
            return at_url.from_str(uri)
        case ["profile", did]:
            return at_url(did)
    return None
