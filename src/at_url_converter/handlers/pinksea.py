from at_url_converter.atproto_utils import get_index, url_obj, at_url

# not sure where the code lives that handles fragments. ctrl-f only gave this https://github.com/shinolabs/PinkSea/blob/master/PinkSea.Frontend/src/api/tegaki/tegaki.js#L1436
hosts = ['pinksea.art']
pinksea = "com.shinolabs.pinksea.oekaki"

async def handler(u: url_obj) -> at_url | None:
    match u:
        case url_obj(path=[repo, _, *rest], fragment=frag):
            if frag:
                frag_repo, _, rkey = frag.rpartition("-")
                return at_url(frag_repo, pinksea, rkey)
            elif repo:
                return at_url(repo, pinksea, get_index(rest, 0))
    return None
