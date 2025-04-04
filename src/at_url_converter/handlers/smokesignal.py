from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['smokesignal.events']

async def handler(u: url_obj) -> at_url | None:
    if repo := u.path_index(0):
        out = at_url(repo)
        if rkey := u.path_index(1):
            out.collection, out.rkey = "events.smokesignal.calendar.event", rkey
        else:
            out.collection, out.rkey = "events.smokesignal.app.profile", "self"
        return out
