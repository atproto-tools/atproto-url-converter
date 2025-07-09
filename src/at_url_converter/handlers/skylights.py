from at_url_converter.atproto_utils import find_query_param, url_obj, at_url
from at_url_converter import lex

hosts = ['skylights.my']

# https://github.com/Gregoor/skylights/blob/main/web/src/utils.ts
built_in_lists = [
    "queue",
    "inProgress",
    "abandoned",
    "owned",
    "wishlist",
]

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["profile", repo]:
            #TODO bug the dev to store his records as type:record in json instead of object so it gets indexed properly
            if u.find_query_param("list"):
                return at_url(repo, "my.skylights.listItem")
            return at_url(repo, lex.skylights.rel)
