from at_url_converter.atproto_utils import get_did, url_obj, at_url
from at_url_converter.boilerplate import get_index

# list of hostnames that potentially match this handler
hosts = ["atproto.camp"]

async def handler(u: url_obj) -> at_url | None:
    if did := await get_did(get_index(u.path, 0)):
        out = at_url(did, "blue.badge.collection") # unpublished
        if rkey := get_index(u.path, 1):
            out.rkey = rkey
        return out
