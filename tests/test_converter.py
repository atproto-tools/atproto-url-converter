import pytest
import at_url_converter
from at_url_converter.atproto_utils import log

@pytest.fixture(autouse=True)
def log_level(monkeypatch):
    log.setLevel("DEBUG")
    # log.logger.addHandler(logging.StreamHandler())

url = "https://klearsky.pages.dev/#/home/starter-pack?uri=at://did:plc:p2cp5gopk7mgjegy6wadk3ep/app.bsky.graph.starterpack/3kztso5fnic24"
atp = "at://did:plc:p2cp5gopk7mgjegy6wadk3ep/app.bsky.graph.starterpack/3kztso5fnic24"
async def test_convert():
    assert str(await at_url_converter.convert(url)) == atp
