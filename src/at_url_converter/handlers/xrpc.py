from at_url_converter.atproto_utils import log, url_obj, at_url

hosts = ['public.api.bsky.app']


params = ["repo", "collection", "rkey"]
def get_params(u: url_obj, required: int):
    found = {}
    for param in params[:required]:
        found[param] = u.find_query_param(param)
    if all(found.values()):
        return at_url(**found)
    else:
        log.warning(f"did not get all components of at_url: got {found}")

async def handler(u: url_obj) -> at_url | None:
    if method := u.path_index(1):
        match method:
            case "com.atproto.repo.getRecord":
                return get_params(u, 3)
            case "com.atproto.repo.listRecords":
                return get_params(u, 2)
            case "com.atproto.sync.listBlobs":
                if did := u.find_query_param("did"):
                    return at_url(did, "blobs")
