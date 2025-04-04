from at_url_converter.atproto_utils import url_obj, at_url
from at_url_converter import lex

hosts = ['plonk.li']

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["u", did]:
            return at_url(did, lex.plonk.paste)
