from at_url_converter.atproto_utils import url_obj, at_url
from at_url_converter.handlers.bluesky import handler as bsky_handler

hosts = ['skyview.social']

async def handler(u: url_obj) -> at_url | None:
    if link := u.find_query_param("url"):
        return await bsky_handler(url_obj(link))
    return None
