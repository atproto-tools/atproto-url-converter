from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['badge.blue']

async def handler(u: url_obj) -> at_url | None:
    if uri := u.find_query_param("uri"):
        return at_url.from_str(uri)
