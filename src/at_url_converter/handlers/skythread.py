from at_url_converter.atproto_utils import url_obj, at_url
from at_url_converter import lex

hosts = ['blue.mackuba.eu']

async def handler(u: url_obj) -> at_url | None:
    if (repo := u.find_query_param("author")) and (rkey := u.find_query_param("post")):
        return at_url(repo, lex.bsky.post, rkey)
