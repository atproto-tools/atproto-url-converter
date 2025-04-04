from at_url_converter.atproto_utils import list_records, log, get_index, url_obj, at_url
hosts = ['whtwnd.com']

collection = "com.whtwnd.blog.entry"

async def handler(u: url_obj) -> at_url | None:
    match u.path:
        case [author]:
            try:
                return at_url(author, collection)
            except ValueError as e:
                log.error(f"whtwind: error parsing {u.og}:\n{e}")
        case[author, "entries", *rest]:
            out = at_url(author, collection)
            if rkey := u.find_query_param("rkey"):
                out.rkey = rkey
            elif title := get_index(rest, 0):
                checked = 0
                recs = list_records(out)
                log.debug(f"searching for {title}")
                async for rec in recs:
                    checked += 1
                    log.debug(f"got post: {rec.value['title']}")
                    if rec.value['title'] == title:
                        log.debug(f"found after searching {checked} recs")
                        out = at_url.from_str(rec.uri)
                        await recs.aclose()
                        return out
                else:
                    log.error(f"could not find a post titled {title}")
                    return None
        case[author, rkey, _]: #blocked include third cid segment once we get them in uris
            return at_url(author, collection, rkey)
