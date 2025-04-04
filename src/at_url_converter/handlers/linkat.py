from at_url_converter.atproto_utils import url_obj, at_url
from at_url_converter.lex import linkat
hosts = ['linkat.blue']

async def handler(u: url_obj) -> at_url | None:
    if repo := u.path_index(0):
        out = at_url(repo, linkat.board, "self")
        return out
