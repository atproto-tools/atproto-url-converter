import pytest
from atproto_core.did_doc import DidDocument
from at_url_converter.atproto_utils import resolver, check_did_handle

# Sample data for testing
VALID_DID = "did:example:123456789abcdefghi"
VALID_HANDLE = "example.com"
INVALID_REPO = "invalid_repo"
VALID_URL = "at://example.com/app.bsky.feed.post/123456789abcdefghi?param=value#fragment"
INVALID_URL = "at://example.com/app.bsky.feed.post/123456789abcdefghi/extra"

@pytest.fixture(autouse=True)
def mock_resolver(monkeypatch):
    handle_resolve = resolver.handle.ensure_resolve
    async def mock_ensure_resolve_handle(handle):
        if handle == VALID_HANDLE:
            return VALID_DID
        return await handle_resolve(handle)

    did_resolve = resolver.did.ensure_resolve
    async def mock_ensure_resolve_did(did):
        if did == VALID_DID:
            return DidDocument(
                id=VALID_DID,
                alsoKnownAs=["at://" + VALID_HANDLE]
            )
        return await did_resolve(did)
    async def mock_check_did_handle(did):
        if did == VALID_DID:
            return VALID_HANDLE, True
        return check_did_handle(did)

    monkeypatch.setattr('at_url_converter.atproto_utils.check_did_handle', mock_check_did_handle)

    monkeypatch.setattr('at_url_converter.atproto_utils.resolver.handle.ensure_resolve', mock_ensure_resolve_handle)
    monkeypatch.setattr('at_url_converter.atproto_utils.resolver.did.ensure_resolve', mock_ensure_resolve_did)
