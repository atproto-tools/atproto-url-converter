from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['internect.info']

async def handler(u: url_obj) -> at_url | None:
    if repo := u.path_index(1):
        return at_url(repo)
