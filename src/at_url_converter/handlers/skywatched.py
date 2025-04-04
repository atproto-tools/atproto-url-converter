from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['skywatched.app']

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["review", uri]:
            return at_url.from_str(uri)
        case ["user", repo]:
            return at_url(repo, "my.skylights.rel") #TODO (already added to lex list)
    return None
