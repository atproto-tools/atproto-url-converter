from at_url_converter.atproto_utils import url_obj, at_url, log
from at_url_converter import lex

hosts = ['skychat.social']

params = {
    "thread": lex.bsky.post,
    "likes": lex.bsky.like,
    "follows": lex.bsky.follow
}


async def handler(u: url_obj) -> at_url | None:
    match u.split_path(u.fragment):
        case [prefix, repo, *rest]:
            out = at_url(repo)
            if collection := params.get(prefix) or lex.bsky.__members__.get(prefix):
                out.collection = collection
            else:
                log.error(f"skychat handler: unknown prefix: {prefix}")
            if len(rest) == 1:
                out.rkey = rest[0]
            else:
                log.error(f"skychat handler: extra elements in path suffix: {rest}")
            return out
