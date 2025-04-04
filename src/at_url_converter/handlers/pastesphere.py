from at_url_converter.atproto_utils import url_obj, at_url
from at_url_converter import lex

hosts = ['pastesphere.link']

async def handler(u: url_obj) -> at_url | None:
    if handle := u.path_index(1):
        out = at_url(handle, lex.pastesphere.snippet)
        if rkey := u.path_index(3):
            out.rkey = rkey
        return out
