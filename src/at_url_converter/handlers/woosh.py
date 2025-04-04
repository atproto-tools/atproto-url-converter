from at_url_converter.atproto_utils import get_index, get_did, url_obj, at_url

hosts = ['woosh.link']

async def handler(u: url_obj) -> at_url | None:
    if did := await get_did(get_index(u.path, 0)):
        return at_url(did)
