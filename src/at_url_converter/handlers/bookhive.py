from at_url_converter.atproto_utils import url_obj, at_url
from at_url_converter.lex import bookhive

hosts = ['bookhive.buzz']

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["profile", repo]:
            return at_url(repo, bookhive.book)
    return None
