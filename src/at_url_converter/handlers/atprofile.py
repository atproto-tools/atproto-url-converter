from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['atprofile.com']

async def handler(u: url_obj) -> at_url | None:
    if repo := u.path_index(0):
        out = at_url(repo, "com.atprofile.beta.profile", "self")
        if await out.get_did(1):
            return out
