from at_url_converter.atproto_utils import get_index, get_did, url_obj, at_url

# list of hostnames that potentially match this handler
hosts = ['atproto-browser.vercel.app']

async def handler(u: url_obj) -> at_url | None:
    path = u.path
    if handle := await get_did(get_index(path, 1)):
        out = at_url(handle, *path[2:])
        return out
