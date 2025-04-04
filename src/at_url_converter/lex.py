from enum import StrEnum

class bsky(StrEnum):
    like = 'app.bsky.feed.like'
    '''[app.bsky.feed.like](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/feed/like.json)'''
    profile = 'app.bsky.actor.profile'
    '''[app.bsky.actor.profile](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/actor/profile.json)'''
    list = 'app.bsky.graph.list'
    '''[app.bsky.graph.list](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/graph/list.json)'''
    listitem = 'app.bsky.graph.listitem'
    '''[app.bsky.graph.listitem](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/graph/listitem.json)'''
    block = 'app.bsky.graph.block'
    '''[app.bsky.graph.block](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/graph/block.json)'''
    service = 'app.bsky.labeler.service'
    '''[app.bsky.labeler.service](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/labeler/service.json)'''
    repost = 'app.bsky.feed.repost'
    '''[app.bsky.feed.repost](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/feed/repost.json)'''
    starterpack = 'app.bsky.graph.starterpack'
    '''[app.bsky.graph.starterpack](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/graph/starterpack.json)'''
    feedgen = 'app.bsky.feed.generator'
    '''[app.bsky.feed.generator](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/feed/generator.json)'''
    threadgate = 'app.bsky.feed.threadgate'
    '''[app.bsky.feed.threadgate](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/feed/threadgate.json)'''
    listblock = 'app.bsky.graph.listblock'
    '''[app.bsky.graph.listblock](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/graph/listblock.json)'''
    follow = 'app.bsky.graph.follow'
    '''[app.bsky.graph.follow](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/graph/follow.json)'''
    postgate = 'app.bsky.feed.postgate'
    '''[app.bsky.feed.postgate](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/feed/postgate.json)'''
    post = 'app.bsky.feed.post'
    '''[app.bsky.feed.post](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/feed/post.json)'''

class universal(StrEnum):
    schema = 'com.atproto.lexicon.schema'
    '''[com.atproto.lexicon.schema](https://github.com/bluesky-social/atproto/tree/main/lexicons/com/atproto/lexicon/schema.json)'''

class bsky_chat(StrEnum):
    declaration = 'chat.bsky.actor.declaration'
    '''[chat.bsky.actor.declaration](https://github.com/bluesky-social/atproto/tree/main/lexicons/chat/bsky/actor/declaration.json)'''

class linkat(StrEnum):
    board = 'blue.linkat.board'
    '''[blue.linkat.board](https://github.com/mkizka/linkat/tree/main/lexicons/blue/linkat/board.json)'''

class whtwnd(StrEnum):
    entry = 'com.whtwnd.blog.entry'
    '''[com.whtwnd.blog.entry](https://github.com/whtwnd/whitewind-blog/tree/main/lexicons/com/whtwnd/blog/entry.json)'''

class frontpage(StrEnum):
    post = 'fyi.unravel.frontpage.post'
    '''[fyi.unravel.frontpage.post](https://github.com/likeandscribe/frontpage/tree/main/lexicons/fyi/unravel/frontpage/post.json)'''
    vote = 'fyi.unravel.frontpage.vote'
    '''[fyi.unravel.frontpage.vote](https://github.com/likeandscribe/frontpage/tree/main/lexicons/fyi/unravel/frontpage/vote.json)'''
    comment = 'fyi.unravel.frontpage.comment'
    '''[fyi.unravel.frontpage.comment](https://github.com/likeandscribe/frontpage/tree/main/lexicons/fyi/unravel/frontpage/comment.json)'''

class statusphere(StrEnum):
    status = 'xyz.statusphere.status'
    '''[xyz.statusphere.status](https://github.com/bluesky-social/statusphere-example-app/tree/main/lexicons/status.json)'''

class smoke_signal(StrEnum):
    profile = 'events.smokesignal.app.profile'
    '''[events.smokesignal.app.profile](https://github.com/SmokeSignal-Events/lexicon/tree/main/events/smokesignal/app/profile.json)'''
    rsvp = 'events.smokesignal.calendar.rsvp'
    '''[events.smokesignal.calendar.rsvp](https://github.com/SmokeSignal-Events/lexicon/tree/main/events/smokesignal/calendar/rsvp.json)'''
    event = 'events.smokesignal.calendar.event'
    '''[events.smokesignal.calendar.event](https://github.com/SmokeSignal-Events/lexicon/tree/main/events/smokesignal/calendar/event.json)'''

class picosky(StrEnum):
    room = 'social.psky.chat.room'
    '''[social.psky.chat.room](https://github.com/psky-atp/appview/tree/main/lexicons/social/psky/chat/room.json)'''
    message = 'social.psky.chat.message'
    '''[social.psky.chat.message](https://github.com/psky-atp/appview/tree/main/lexicons/social/psky/chat/message.json)'''
    profile = 'social.psky.actor.profile'
    '''[social.psky.actor.profile](https://github.com/psky-atp/appview/tree/main/lexicons/social/psky/actor/profile.json)'''

class atfile(StrEnum):
    lock = 'blue.zio.atfile.lock'
    '''[blue.zio.atfile.lock](https://github.com/ziodotsh/lexicons/tree/main/blue/zio/atfile/lock.json)'''
    upload = 'blue.zio.atfile.upload'
    '''[blue.zio.atfile.upload](https://github.com/ziodotsh/lexicons/tree/main/blue/zio/atfile/upload.json)'''

class pin_boards(StrEnum):
    tagged = 'xyz.jeroba.tags.tagged'
    '''[xyz.jeroba.tags.tagged](https://github.com/not-nan/atags/tree/main/lexicons/xyz/jeroba/tags/tagged.json)'''
    tag = 'xyz.jeroba.tags.tag'
    '''[xyz.jeroba.tags.tag](https://github.com/not-nan/atags/tree/main/lexicons/xyz/jeroba/tags/tag.json)'''

class bookhive(StrEnum):
    buzz = 'buzz.bookhive.buzz'
    '''[buzz.bookhive.buzz](https://github.com/nperez0111/bookhive/tree/main/lexicons/buzz.json)'''
    book = 'buzz.bookhive.book'
    '''[buzz.bookhive.book](https://github.com/nperez0111/bookhive/tree/main/lexicons/book.json)'''
    hiveBook = 'buzz.bookhive.hiveBook'
    '''[buzz.bookhive.hiveBook](https://github.com/nperez0111/bookhive/tree/main/lexicons/hiveBook.json)'''

class bluemoji(StrEnum):
    pack = 'blue.moji.packs.pack'
    '''[blue.moji.packs.pack](https://github.com/aendra-rininsland/bluemoji/tree/main/schema/blue.moji/packs/pack.json)'''
    packitem = 'blue.moji.packs.packitem'
    '''[blue.moji.packs.packitem](https://github.com/aendra-rininsland/bluemoji/tree/main/schema/blue.moji/packs/packitem.json)'''
    item = 'blue.moji.collection.item'
    '''[blue.moji.collection.item](https://github.com/aendra-rininsland/bluemoji/tree/main/schema/blue.moji/collection/item.json)'''

class pinksea(StrEnum):
    oekaki = 'com.shinolabs.pinksea.oekaki'
    '''[com.shinolabs.pinksea.oekaki](https://github.com/shinolabs/PinkSea/tree/master/PinkSea.Lexicons/com/shinolabs/pinksea/oekaki.json)'''

class plonk(StrEnum):
    paste = 'li.plonk.paste'
    '''[li.plonk.paste](https://github.com/oppiliappan/plonk/tree/master/lexicons/paste.json)'''
    comment = 'li.plonk.comment'
    '''[li.plonk.comment](https://github.com/oppiliappan/plonk/tree/master/lexicons/comment.json)'''

class atprofile(StrEnum):
    profile = 'com.atprofile.beta.profile'
    '''[com.atprofile.beta.profile](https://github.com/Narkoleptika/atprofile.com/tree/main/src/lexicon/definitions/com.atprofile.beta.profile.json)'''

class pastesphere(StrEnum):
    snippet = 'link.pastesphere.snippet'
    '''[link.pastesphere.snippet](https://github.com/echo8/pastesphere/tree/main/lexicons/snippet.json)'''

class recipe_exchange(StrEnum):
    recipe = 'exchange.recipe.recipe'
    '''[exchange.recipe.recipe](https://recipe.exchange/lexicons/recipe.json)'''
    collection = 'exchange.recipe.collection'
    '''[exchange.recipe.collection](https://recipe.exchange/lexicons/collection.json)'''
    comment = 'exchange.recipe.comment'
    '''exchange.recipe.comment'''
    profile = 'exchange.recipe.profile'
    '''exchange.recipe.profile'''
