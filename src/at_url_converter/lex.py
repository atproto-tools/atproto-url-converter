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
    labeler = 'app.bsky.labeler.service'
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
    verification = 'app.bsky.graph.verification'
    '''[app.bsky.graph.verification](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/graph/verification.json)'''
    status = 'app.bsky.actor.status'
    '''[app.bsky.actor.status](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky/actor/status.json)'''

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
    board = 'xyz.jeroba.tags.tagged'
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
    '''[exchange.recipe.profile](https://recipe.exchange/lexicons/profile.json)'''

class skylights(StrEnum):
    rel = 'my.skylights.rel'
    '''[my.skylights.rel](https://github.com/Gregoor/skylights/tree/main/lexicons/rel.json)'''

class tangled(StrEnum):
    follow = 'sh.tangled.graph.follow'
    '''[sh.tangled.graph.follow](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/graph/follow.json)'''
    issue_comment = 'sh.tangled.repo.issue.comment'
    '''[sh.tangled.repo.issue.comment](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/issue/comment.json)'''
    issue = 'sh.tangled.repo.issue'
    '''[sh.tangled.repo.issue](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/issue/issue.json)'''
    state = 'sh.tangled.repo.issue.state'
    '''[sh.tangled.repo.issue.state](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/issue/state.json)'''
    knot_member = 'sh.tangled.knot.member'
    '''[sh.tangled.knot.member](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/knot/member.json)'''
    publicKey = 'sh.tangled.publicKey'
    '''[sh.tangled.publicKey](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/publicKey.json)'''
    pull_comment = 'sh.tangled.repo.pull.comment'
    '''[sh.tangled.repo.pull.comment](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/pulls/comment.json)'''
    pull = 'sh.tangled.repo.pull'
    '''[sh.tangled.repo.pull](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/pulls/pull.json)'''
    pull_status = 'sh.tangled.repo.pull.status'
    '''[sh.tangled.repo.pull.status](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/pulls/state.json)'''
    repo = 'sh.tangled.repo'
    '''[sh.tangled.repo](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/repo.json)'''
    star = 'sh.tangled.feed.star'
    '''[sh.tangled.feed.star](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/feed/star.json)'''
    profile = 'sh.tangled.actor.profile'
    '''[sh.tangled.actor.profile](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/actor/profile.json)'''
    artifact = 'sh.tangled.repo.artifact'
    '''[sh.tangled.repo.artifact](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/artifact.json)'''
    refUpdate = 'sh.tangled.git.refUpdate'
    '''[sh.tangled.git.refUpdate](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/git/refUpdate.json)'''
    pipeline = 'sh.tangled.pipeline'
    '''[sh.tangled.pipeline](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/pipeline.json)'''
    pipeline_status = 'sh.tangled.pipeline.status'
    '''[sh.tangled.pipeline.status](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/pipeline/status.json)'''
    spindle_member = 'sh.tangled.spindle.member'
    '''[sh.tangled.spindle.member](https://tangled.sh/@tangled.sh/core/blob/master/lexicons/spindle/member.json)'''

class flo_bit(StrEnum):
    room = 'dev.flo-bit.room'
    '''dev.flo-bit.room'''

class blue_place(StrEnum):
    pixel = 'blue.place.pixel'
    '''[blue.place.pixel](https://github.com/QuietImCoding/place.blue/tree/main/atproto/lexicons/pixel.json)'''

class teal(StrEnum):
    status = 'fm.teal.alpha.actor.status'
    '''[fm.teal.alpha.actor.status](https://github.com/teal-fm/teal/tree/main/packages/lexicons/real/fm/teal/alpha/actor/status.json)'''
    play = 'fm.teal.alpha.feed.play'
    '''[fm.teal.alpha.feed.play](https://github.com/teal-fm/teal/tree/main/packages/lexicons/real/fm/teal/alpha/feed/play.json)'''
    profile = 'fm.teal.alpha.actor.profile'
    '''[fm.teal.alpha.actor.profile](https://github.com/teal-fm/teal/tree/main/packages/lexicons/real/fm/teal/alpha/actor/profile.json)'''

class leaflet(StrEnum):
    document = 'pub.leaflet.document'
    '''[pub.leaflet.document](https://github.com/hyperlink-academy/leaflet/tree/main/lexicons/pub/leaflet/document.json)'''
    publication = 'pub.leaflet.publication'
    '''[pub.leaflet.publication](https://github.com/hyperlink-academy/leaflet/tree/main/lexicons/pub/leaflet/publication.json)'''
    subscription = 'pub.leaflet.graph.subscription'
    '''[pub.leaflet.graph.subscription](https://github.com/hyperlink-academy/leaflet/tree/main/lexicons/pub/leaflet/graph/subscription.json)'''

class navyfragen(StrEnum):
    message = 'app.navyfragen.message'
    '''[app.navyfragen.message](https://github.com/karanshukla/navyfragen-app/tree/main/server/lexicons/message.json)'''

class blebbit(StrEnum):
    page = 'app.blebbit.authr.page.record'
    '''[app.blebbit.authr.page.record](https://pdsls.dev/at://did:plc:veavz5io7eocwh7dbrhr2thi/com.atproto.lexicon.schema/app.blebbit.authr.page.record)'''
    group = 'app.blebbit.authr.group.record'
    '''[app.blebbit.authr.group.record](https://pdsls.dev/at://did:plc:veavz5io7eocwh7dbrhr2thi/com.atproto.lexicon.schema/app.blebbit.authr.group.record)'''
    folder = 'app.blebbit.authr.folder.record'
    '''[app.blebbit.authr.folder.record](https://pdsls.dev/at://did:plc:veavz5io7eocwh7dbrhr2thi/com.atproto.lexicon.schema/app.blebbit.authr.folder.record)'''

class grain(StrEnum):
    favorite = 'social.grain.favorite'
    '''[social.grain.favorite](https://tangled.sh/@grain.social/grain/blob/main/lexicons/social/grain/favorite.json)'''
    gallery = 'social.grain.gallery'
    '''[social.grain.gallery](https://tangled.sh/@grain.social/grain/blob/main/lexicons/social/grain/gallery/gallery.json)'''
    item = 'social.grain.gallery.item'
    '''[social.grain.gallery.item](https://tangled.sh/@grain.social/grain/blob/main/lexicons/social/grain/gallery/item.json)'''
    exif = 'social.grain.photo.exif'
    '''[social.grain.photo.exif](https://tangled.sh/@grain.social/grain/blob/main/lexicons/social/grain/photo/exif.json)'''
    photo = 'social.grain.photo'
    '''[social.grain.photo](https://tangled.sh/@grain.social/grain/blob/main/lexicons/social/grain/photo/photo.json)'''
    follow = 'social.grain.graph.follow'
    '''[social.grain.graph.follow](https://tangled.sh/@grain.social/grain/blob/main/lexicons/social/grain/graph/follow.json)'''
    service = 'social.grain.labeler.service'
    '''[social.grain.labeler.service](https://tangled.sh/@grain.social/grain/blob/main/lexicons/social/grain/labelers/service.json)'''
    profile = 'social.grain.actor.profile'
    '''[social.grain.actor.profile](https://tangled.sh/@grain.social/grain/blob/main/lexicons/social/grain/actor/profile.json)'''

class atpage(StrEnum):
    page = 'one.atpage.page'
    '''[one.atpage.page](https://github.com/danloh/atpage/tree/main/lexicons/page.json)'''

class grayhaze(StrEnum):
    hls = 'live.grayhaze.format.hls'
    '''[live.grayhaze.format.hls](https://github.com/hugeblank/grayhaze.live/tree/main/lexicons/live/grayhaze/format/hls.json)'''
    ban = 'live.grayhaze.interaction.ban'
    '''[live.grayhaze.interaction.ban](https://github.com/hugeblank/grayhaze.live/tree/main/lexicons/live/grayhaze/interaction/ban.json)'''
    stream = 'live.grayhaze.content.stream'
    '''[live.grayhaze.content.stream](https://github.com/hugeblank/grayhaze.live/tree/main/lexicons/live/grayhaze/content/stream.json)'''
    emote = 'live.grayhaze.content.emote'
    '''[live.grayhaze.content.emote](https://github.com/hugeblank/grayhaze.live/tree/main/lexicons/live/grayhaze/content/emote.json)'''
    follow = 'live.grayhaze.interaction.follow'
    '''[live.grayhaze.interaction.follow](https://github.com/hugeblank/grayhaze.live/tree/main/lexicons/live/grayhaze/interaction/follow.json)'''
    promotion = 'live.grayhaze.interaction.promotion'
    '''[live.grayhaze.interaction.promotion](https://github.com/hugeblank/grayhaze.live/tree/main/lexicons/live/grayhaze/interaction/promotion.json)'''
    chat = 'live.grayhaze.interaction.chat'
    '''[live.grayhaze.interaction.chat](https://github.com/hugeblank/grayhaze.live/tree/main/lexicons/live/grayhaze/interaction/chat.json)'''
    channel = 'live.grayhaze.actor.channel'
    '''[live.grayhaze.actor.channel](https://github.com/hugeblank/grayhaze.live/tree/main/lexicons/live/grayhaze/actor/channel.json)'''
