from at_url_converter.atproto_utils import url_obj, at_url
hosts = ['skyblur.uk']

async def handler(u: url_obj) -> at_url | None:
    if repo := u.path_index(1):
        out = at_url(repo, "uk.skyblur.post") #TODO
        if rkey := u.path_index(2):
            out.rkey = rkey
        return out
