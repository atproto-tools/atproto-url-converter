from at_url_converter.atproto_utils import url_obj, at_url
from at_url_converter import lex

hosts = ['ruthub.com']

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["kb", repo]:
            return at_url(repo, "com.ruthub.kanban") #TODO
        case ["blog", repo]:
            return at_url(repo, "com.ruthub.entry")
        case ["p", repo, rkey]:
            return at_url(repo, "com.ruthub.entry", rkey)
        case ["rut", repo]:
            return at_url(repo, "com.ruthub.item")
