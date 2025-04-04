from at_url_converter.atproto_utils import get_did, url_obj, at_url
from at_url_converter.boilerplate import get_index

hosts = ['flushes.app']

async def handler(u: url_obj) -> at_url | None:
    if did := await get_did(get_index(u.path, 1)):
        return at_url(did)
