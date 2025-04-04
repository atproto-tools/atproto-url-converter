to add a handler:

1. Install dependencies `pip install '.[dev]'`.
1. Add (hopefully comprehensive) test cases to [the test cases dir](/handler_test_cases/) - the format is simple, a list of [source, dest] url pairs. The filename of the test case must exactly match name of the corresponding handler.
1. (optional but encouraged) If the site uses a lexicon not already in [lex.py](/src/at_url_converter/lex.py), add it manually or edit the atproto-tools [record types table](https://atproto-tools.getgrist.com/p2SiVPSGqbi8/atproto-tools/p/33) and run [lex_gen.py](/src/lex_gen.py).
1. Write a handler that passes the test cases. See the [template](/src/at_url_converter/handlers/_template.py) for reference.
1. Add it to [the handlers lookup key](/src/at_url_converter/handlers_lookup.py).
1. Test with pytest.
