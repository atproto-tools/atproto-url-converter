from at_url_converter.atproto_utils import log, url_obj, at_url

# list of hostnames that potentially match this handler
hosts = []

async def handler(u: url_obj) -> at_url | None:
    if did := u.path_index(1):
        log.debug(f'handler got {did} from {u.path[1]}')
        return at_url(did)
