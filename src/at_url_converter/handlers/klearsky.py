from urllib.parse import unquote
from at_url_converter.atproto_utils import log, url_obj, at_url
from at_url_converter.boilerplate import get_index
from at_url_converter import lex
# source https://github.com/mimonelu/klearsky/blob/staging/src/router/index.ts
# also https://github.com/mimonelu/klearsky/blob/staging/src/views/MainView.vue#L498 ?
# after a while looking at the code i couldn't determine the routing logic (where are url params processed?)
# however i did find this function which partially covers it https://github.com/mimonelu/klearsky/blob/staging/src/components/labels/HtmlText.vue#L99
# edit: after looking at it again, apparently there's just no central function. just search for it instead https://github.com/search?q=repo%3Amimonelu%2Fklearsky%20state.currentQuery&type=code

hosts = ["klearsky.pages.dev"]


async def handler(u: url_obj) -> at_url | None:
    frag = u.fragment.split("?")
    if len(frag) != 2:
        log.error(f"got weird klearsky url, investigate: {u.og}")
        return None
    u.path, u.query = url_obj.split_path(frag[0]), url_obj.parse_query(frag[1])

    if uri := next((v for p in ["uri", "list", "feed"] if (v := u.find_query_param(p))), None):
        return at_url.from_str(unquote(uri))
    elif account := u.find_query_param("account"):
        out = at_url(account)
        match u.path_index(0):
            case "profile":
                match get_index(u.path, 1):
                    case "following":
                        out.collection = lex.bsky.follow
                    case "list":
                        out.collection = lex.bsky.list
                    case "feed-generators":
                        out.collection = lex.bsky.feedgen
                    case "feeds":
                        out.collection = lex.bsky.post
                    case None:
                        pass
                    case _ as suffix:
                        log.error(
                            f"error in klearsky when handling {u.og}:\n"
                            f"unknown suffix: {suffix}"
                        )
                        return None
                return out
    elif (handle := u.find_query_param("handle")) and (rkey := u.find_query_param("rkey")):
            return at_url(handle, lex.bsky.post, rkey)
    else:
        return None
