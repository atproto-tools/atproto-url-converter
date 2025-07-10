from typing import Literal, cast
from at_url_converter.handlers_lookup import handlers_lookup
from at_url_converter.atproto_utils import at_url, url_obj, get_record, get_did, httpx_client, log
from bs4 import BeautifulSoup
from bs4.filter import SoupStrainer
import os
#TODO add optional lxml dependency
# [project.optional-dependencies]
# PDF = ["ReportLab>=1.2", "RXP"]
#TODO document these in readme
OPT_RESOLVE_AS_HANDLE = int(os.environ.get("AT_URL_CONVERTER_RESOLVE_AS_HANDLE", 0))
OPT_CHECK_HTML = int(os.environ.get("AT_URL_CONVERTER_CHECK_HTML", 1))
OPT_FETCH_DID = cast(Literal[0,1,2], int(os.environ.get("AT_URL_CONVERTER_FETCH_DID", 0)))

link_strainer = SoupStrainer(
    'link', 
    attrs={
        'rel': 'alternate', 
        'href': lambda value: bool(value) and value.startswith('at://')
    }
)

async def convert(
    url: str,
    fetch_did: Literal[0, 1, 2] = OPT_FETCH_DID,
    check_html=OPT_CHECK_HTML,
    resolve_as_handle=OPT_RESOLVE_AS_HANDLE
) -> at_url | None:
    '''
    translate a https:// url to its at:// equivalent. Occasionally needs one or several network requests.

    Args:
        url (str): the http url to convert
        fetch_did (bool): whether to fetch the did for the resulting at_url
        check_html (bool): whether to check the html for <link rel="alternate" href="at://..."> tags
        resolve_as_handle (bool): whether to resolve the hostname as a handle
    Returns:
        at_url: the resulting url
    '''    
    u = url_obj(url)
    netloc = u.netloc
    out = None
    if handler := handlers_lookup.get(netloc):
        log.debug(msg=f"invoking handler {handler.__module__.split(".")[-1]} for {netloc}")
        out = await handler(u)
    if not out and check_html:
        log.info(f"looking for at:// <link>s in {url}")
        r = await httpx_client.get(url)
        parsed = BeautifulSoup(r.text, features="html.parser", parse_only=link_strainer)
        if links := [link.get("href") for link in parsed.find_all()]: #type: ignore - selector makes sure it's going to have a href
            if len(links) > 1:
                log.warning(f"found multiple links in html:\n{links}")
            out = at_url.from_str(links[0]) #type: ignore - it's going to be a string
    if not out and resolve_as_handle:
        log.info(f"trying to resolve {netloc} as handle")
        if did := await get_did(netloc):
            out = at_url(repo=did)
    if not out:
        log.info(f"tranlsation failed for {url}")
        return None
    if fetch_did:
        await out.get_did(fetch_did)
    return out

async def convert_and_fetch(
    url_str: str,
    fetch_did: Literal[0, 1, 2] = OPT_FETCH_DID,
    check_html=OPT_CHECK_HTML,
    resolve_as_handle=OPT_RESOLVE_AS_HANDLE
):
    if url := await convert(url_str, fetch_did, check_html, resolve_as_handle=resolve_as_handle):
        return await get_record(url)

cli_help = "Atttempt to convert a https:// URL to its at:// equivalent"

fallback_help = """0 - only use handlers
1 - (default) if there is no existing handler for the given url, fetch the url contents
    and look for a <link rel="alternate" href="at://..."> in the html tags
2 - if no <link> tags found, try to resolve the url's hostname as a handle
"""


#TODO write proper tests
def cli():
    import argparse
    import asyncio
    parser = argparse.ArgumentParser(description=cli_help, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-d", "--fetch-did", nargs="?", const=0, choices=[0,1,2], help="fetch the did for the resulting at_url if there isn't one (0 - no, 1 - yes, 2 - yes, and verify it). defaults to 0")
    parser.add_argument("-f", "--fallback", nargs="?", const=0, type=int, choices=[0,1,2], help=fallback_help)
    parser.add_argument("-g", "--get", action="store_true", help="fetch the record after converting (url must have rkey)")
    parser.add_argument("-l", "--log-level", nargs="?", const="INFO", help="enable logging (when enabled, default to INFO)")
    parser.add_argument("url", help="the URL to convert.", nargs="?")
    args = parser.parse_args()
    try:
        if args.level:
            if ":" in args.level:
                args.url = args.level
                args.level = "info"

            from logging import StreamHandler
            log.logger.addHandler(StreamHandler())
            log.setLevel(args.level.upper())
        fallback_list: list[Literal[0, 1, 2]] = []
        match args.fallback:
            case 1:
                fallback_list = [1, 0]
            case 2:
                fallback_list = [1, 1]
        if args.get:
            r = asyncio.run(convert_and_fetch(args.url, *fallback_list))
            if r:
                print(r.model_dump_json(indent=2))
        elif args.url:
            print(asyncio.run(convert(args.url)))
        else:
            parser.print_help()
    except Exception as e:
        if log.getEffectiveLevel() > 10:
            e.__traceback__ = None
        import sys
        print(e, file=sys.stderr)

if __name__ == "__main__":
    cli()
