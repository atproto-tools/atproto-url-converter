from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['atp.tools']

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["at:", repo, *rest]:
            out = at_url(repo)
            if rest:
                out.collection = rest[0]
            return out
    return None
