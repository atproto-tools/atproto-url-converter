from at_url_converter.handlers.aglais import handler as aglais
from at_url_converter.handlers.atbrowser import handler as atbrowser
from at_url_converter.handlers.atprofile import handler as atprofile
from at_url_converter.handlers.atprotocamp import handler as atprotocamp
from at_url_converter.handlers.atptools import handler as atptools
from at_url_converter.handlers.bluebadge import handler as bluebadge
from at_url_converter.handlers.bluesky import handler as bluesky
from at_url_converter.handlers.blueviewer import handler as blueviewer
from at_url_converter.handlers.bookhive import handler as bookhive
from at_url_converter.handlers.bskycdn import handler as bskycdn
from at_url_converter.handlers.clearsky import handler as clearsky
from at_url_converter.handlers.flushes import handler as flushes
from at_url_converter.handlers.frontpage import handler as frontpage
from at_url_converter.handlers.internect import handler as internect
from at_url_converter.handlers.klearsky import handler as klearsky
from at_url_converter.handlers.linkat import handler as linkat
from at_url_converter.handlers.myb import handler as myb
from at_url_converter.handlers.ouranos import handler as ouranos
from at_url_converter.handlers.pastesphere import handler as pastesphere
from at_url_converter.handlers.pinboards import handler as pinboards
from at_url_converter.handlers.pinksea import handler as pinksea
from at_url_converter.handlers.pinksky import handler as pinksky
from at_url_converter.handlers.plonk import handler as plonk
from at_url_converter.handlers.popsky import handler as popsky
from at_url_converter.handlers.recipeexchange import handler as recipeexchange
from at_url_converter.handlers.ruthub import handler as ruthub
from at_url_converter.handlers.skyblur import handler as skyblur
from at_url_converter.handlers.skychat import handler as skychat
from at_url_converter.handlers.skylights import handler as skylights
from at_url_converter.handlers.skythread import handler as skythread
from at_url_converter.handlers.skyview import handler as skyview
from at_url_converter.handlers.skywatched import handler as skywatched
from at_url_converter.handlers.smokesignal import handler as smokesignal
from at_url_converter.handlers.supercoolclient import handler as supercoolclient
from at_url_converter.handlers.swablu import handler as swablu
from at_url_converter.handlers.tangled import handler as tangled
from at_url_converter.handlers.whitewind import handler as whitewind
from at_url_converter.handlers.woosh import handler as woosh
from at_url_converter.handlers.xrpc import handler as xrpc


handlers_lookup = {
    "aglais.pages.dev": aglais,
    "atproto-browser.vercel.app": atbrowser,
    "atprofile.com": atprofile,
    "atproto.camp": atprotocamp,
    "atp.tools": atptools,
    "badge.blue": bluebadge,
    "bsky.app": bluesky,
    "main.bsky.dev": bluesky,
    "langit.pages.dev": bluesky,
    "tokimekibluesky.vercel.app": bluesky,
    "blueviewer.pages.dev": blueviewer,
    "bookhive.buzz": bookhive,
    "cdn.bsky.app": bskycdn,
    "video.bsky.app": bskycdn,
    "clearsky.app": clearsky,
    "flushes.app": flushes,
    "frontpage.fyi": frontpage,
    "internect.info": internect,
    "klearsky.pages.dev": klearsky,
    "linkat.blue": linkat,
    "myb.zeu.dev": myb,
    "useouranos.app": ouranos,
    "pastesphere.link": pastesphere,
    "pinboards.jeroba.xyz": pinboards,
    "pinksea.art": pinksea,
    "pinksky.app": pinksky,
    "psky.co": pinksky,
    "plonk.li": plonk,
    "popsky.social": popsky,
    "recipe.exchange": recipeexchange,
    "ruthub.com": ruthub,
    "skyblur.uk": skyblur,
    "skychat.social": skychat,
    "skylights.my": skylights,
    "blue.mackuba.eu": skythread,
    "skyview.social": skyview,
    "skywatched.app": skywatched,
    "smokesignal.events": smokesignal,
    "supercoolclient.pages.dev": supercoolclient,
    "swablu.pages.dev": swablu,
    "tangled.sh": tangled,
    "whtwnd.com": whitewind,
    "woosh.link": woosh,
    "public.api.bsky.app": xrpc,
}
