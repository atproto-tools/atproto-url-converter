# at-url-converter
converts http links from various websites into equivalent atproto links. 

how it works: links are matched by hostname to a [handler](/src/at_url_converter/handlers/). if there is no handler for the given url, fetch the url contents and look for a `<link rel="alternate" href="at://...">` in the html tags. As a last resort, we can try to resolve the url as an atproto handle.

### installation:
(no pypi package yet)
```
pip install https://github.com/atproto-tools/atproto-url-converter/archive/refs/heads/main.zip
```

### usage:

#### cli: 
```bash
convert-at-url https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l
# at://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.post/3l6oveex3ii2l
```

#### python:
```python
import at_url_converter
import asyncio
asyncio.run(at_url_converter.convert("https://useouranos.app/dashboard/user/pouriade.com"))
# at_url(repo='did:plc:3sapfnszmvjc6wa4ml3ybkwb', collection='app.bsky.actor.profile', rkey='self')
```
