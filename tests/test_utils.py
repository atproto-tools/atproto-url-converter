import pytest
import at_url_converter.atproto_utils as atproto_utils
from at_url_converter.atproto_utils import at_url
from conftest import VALID_DID, VALID_HANDLE, INVALID_REPO, VALID_URL, INVALID_URL


async def test_at_url_initialization():
    # Test initialization with valid DID
    uri = at_url(repo=VALID_DID)
    assert uri.did == VALID_DID
    assert uri.handle == ""

    # Test initialization with valid handle
    uri = at_url(repo=VALID_HANDLE)
    assert uri.handle == VALID_HANDLE
    assert uri.did == ""

    # Test initialization with invalid repo
    with pytest.raises(ValueError):
        at_url(repo=INVALID_REPO)

async def test_at_url_from_str():
    # Test parsing a valid URL
    uri = at_url.from_str(VALID_URL)
    assert uri.repo == "example.com"
    assert uri.collection == "app.bsky.feed.post"
    assert uri.rkey == "123456789abcdefghi"
    assert uri.query == [("param", "value")]
    assert uri.fragment == "fragment"

    # Test parsing an invalid URL
    with pytest.raises(ValueError):
        at_url.from_str(INVALID_URL)

async def test_at_url_properties():
    # Test repo property
    uri = at_url(repo=VALID_DID)
    assert uri.repo == VALID_DID

    uri = at_url(repo=VALID_HANDLE)
    assert uri.repo == VALID_HANDLE

    # Test repo property with missing repo
    uri = at_url(repo=VALID_DID)
    uri.did = ""
    with pytest.raises(AttributeError):
        _ = uri.repo

async def test_at_url_get_handle(mock_resolver):
    uri = at_url(repo=VALID_DID)
    handle = await uri.get_handle(verify=0)
    assert handle == VALID_HANDLE  # Replace with actual expected handle

    handle = await uri.get_handle(verify=1)
    assert handle == VALID_HANDLE  # Replace with actual expected handle

    handle = await uri.get_handle(verify=2)
    assert handle == VALID_HANDLE  # Replace with actual expected handle

async def test_at_url_get_did(mock_resolver):
    uri = at_url(repo=VALID_HANDLE)
    did = await uri.get_did(verify=0)
    assert did == VALID_DID  # Replace with actual expected DID

    did = await uri.get_did(verify=1)
    assert did == VALID_DID  # Replace with actual expected DID

    did = await uri.get_did(verify=2)
    assert did == VALID_DID  # Replace with actual expected DID

async def test_at_url_iter():
    uri = at_url(repo=VALID_DID, collection="app.bsky.feed.post", rkey="123456789abcdefghi", query="param=value", fragment="fragment")
    parts = [i for i in uri]
    assert parts == [
        ("did", VALID_DID),
        ("collection", "app.bsky.feed.post"),
        ("rkey", "123456789abcdefghi"),
        ("query", [("param", "value")]),
        ("fragment", "fragment"),
        ("handle", ""), # this is clunky, but idk if it's a good idea to make custom iterators that exclude falsey values
    ]


async def test_at_url_eq():
    uri1 = at_url(repo=VALID_DID, collection="app.bsky.feed.post", rkey="123456789abcdefghi", query="param=value", fragment="fragment")
    uri2 = at_url(repo=VALID_DID, collection="app.bsky.feed.post", rkey="123456789abcdefghi", query="param=value", fragment="fragment")
    uri3 = at_url(repo=VALID_HANDLE, collection="app.bsky.feed.post", rkey="123456789abcdefghi", query="param=value", fragment="fragment")

    assert uri1 == uri2
    assert uri1 != uri3

async def test_at_url_str():
    uri = at_url(repo=VALID_DID, collection="app.bsky.feed.post", rkey="123456789abcdefghi", query="param=value", fragment="fragment")
    assert str(uri) == "at://did:example:123456789abcdefghi/app.bsky.feed.post/123456789abcdefghi?param=value#fragment"

async def test_at_url_repr():
    uri = at_url(repo=VALID_DID, collection="app.bsky.feed.post", rkey="123456789abcdefghi", query="param=value", fragment="fragment", handle=VALID_HANDLE)
    # assert uri.__repr__() == "at_url(did='did:example:123456789abcdefghi', collection='app.bsky.feed.post', rkey='123456789abcdefghi', query=[('param', 'value')], fragment='fragment', handle='example.com')"
    assert uri.__repr__() == "at_url(did='did:example:123456789abcdefghi', collection='app.bsky.feed.post', rkey='123456789abcdefghi', handle='example.com')"
    uri = at_url(repo='did:example:123456789abcdefghi', collection='app.bsky.feed.post')
    assert uri.__repr__() == "at_url(did='did:example:123456789abcdefghi', collection='app.bsky.feed.post')"

async def test_get_pds():
    print(await atproto_utils.get_pds("aeshna-cyanea.bsky.social"))
