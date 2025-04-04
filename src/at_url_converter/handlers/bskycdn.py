from at_url_converter.atproto_utils import url_obj, at_url

hosts = ['cdn.bsky.app', 'video.bsky.app']

async def handler(u: url_obj) -> at_url | None:
    match u:
        case url_obj(netloc="cdn.bsky.app"):
            if repo := u.path_index(3):
                return at_url(repo, "blobs")
        case url_obj(netloc="video.bsky.app"):
            if repo := u.path_index(1):
                return at_url(repo, "blobs")
    return None
