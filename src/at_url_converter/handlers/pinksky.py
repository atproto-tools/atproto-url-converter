from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['pinksky.app', 'psky.co']


async def handler(u: url_obj) -> at_url | None:
    match u:
        case url_obj(netloc="psky.co", path=[repo]):
            return at_url(repo)
        case url_obj(netloc="pinksky.app") as pinksky:
            match pinksky:
                case url_obj(path=[_, *path]):
                    if uri := u.find_query_param("uri") or u.find_query_param("comments"):
                        return at_url.from_str(uri)
                    if path:
                        return at_url(*path)
    return None
