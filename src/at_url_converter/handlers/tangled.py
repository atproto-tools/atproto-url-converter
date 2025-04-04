from at_url_converter.atproto_utils import url_obj, at_url, find_record, log
from at_url_converter import lex

hosts = ['tangled.sh']

async def handler(u: url_obj) -> at_url | None:
    if repo := u.path_index(0):
        out = at_url(repo, "sh.tangled.repo") # TODO
        if tangled_repo := u.path_index(1):
            log.debug(f"searching for {tangled_repo}")
            if rec := await find_record(out, {'name': tangled_repo}):
                return at_url.from_str(rec.uri)
            else:
                log.error(f"could not find repo named {tangled_repo} in {out}")
        else:
            return out
    return None
