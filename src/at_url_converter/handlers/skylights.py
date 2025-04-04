from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['skylights.my']

async def handler(u: url_obj) -> at_url | None:
    if handle := u.path_index(1):
        return at_url(handle, "my.skylights.rel") #TODO
