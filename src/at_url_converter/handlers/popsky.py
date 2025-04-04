from at_url_converter.atproto_utils import get_index, url_obj, at_url

hosts = ['popsky.social']

async def handler(u: url_obj) -> at_url | None:
    if uri := get_index(u.path, 1):
        return at_url.from_str(uri)
