from at_url_converter.atproto_utils import  url_obj, at_url, log
from at_url_converter import lex

hosts = ['recipe.exchange']

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["profiles", repo]:
            return at_url(repo, lex.recipe_exchange.recipe)
        case ["profiles", repo, suffix]:
            if nsid := lex.recipe_exchange.__members__.get(suffix + "s"):
                return at_url(repo, nsid)
            else:
                log.error(f"unkown suffix {suffix} in url {u.og}")
    return None
