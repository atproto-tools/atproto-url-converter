from at_url_converter.atproto_utils import url_obj, at_url
from at_url_converter import lex

hosts = ['myb.zeu.dev']

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case ["p", repo, "stats"]:
            return at_url(repo)
        case ["p", repo, *rest]:
            out = at_url(repo)
            if len(rest) == 1:
                out.collection, out.rkey = lex.bsky.post, rest[0]
            return out
    return None

#TODO what is going ON in the third test case https://myb.zeu.dev/?iss=https%3A%2F%2Fbsky.social&state=irWF0wPDsfUb-eHIVBw0qg&code=cod-f41b1cbf3aa4623e72fea7ee9381dc5c8f26571b2f76c51b1de16ebe56cad447
