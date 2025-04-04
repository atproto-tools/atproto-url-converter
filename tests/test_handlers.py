from collections.abc import Awaitable, Callable
import json
import pytest
import inspect
from at_url_converter.atproto_utils import url_obj, at_url, log
from at_url_converter import convert
from handlers_lookup_gen import modules

log.setLevel("DEBUG")
test_case_dir = "handler_test_cases"

async def handler_to_str(handler: Callable[[url_obj], Awaitable[at_url | None]], val: str):
    result = await handler(url_obj(val))
    if result:
        await result.get_did()
    assert isinstance(result, at_url) or result is None, f"handler must return at_url object, instead returned {result}"
    if result:
        return str(result)

def get_test_cases():
    """Find all modules with handler functions and test cases."""
    test_params = []
    for module in modules:
        module_name = module.__name__.split(".")[-1]
        if inspect.iscoroutinefunction(module.handler): # trust no one, not even yourself
            test_cases = json.load(open((f"{test_case_dir}/{module_name}.json")))
            for i, test_case in enumerate(test_cases):
                match test_case:
                    case [str(), str()]:
                        test_params.append((module, test_case, i))
                    case _:
                        raise ValueError(f"unexpected shape of test case {i} in {module_name}: {test_case}")
        else:
            raise ValueError(f"module {module_name} handler is not an async function")
    return test_params

@pytest.mark.parametrize("module,case,case_index", get_test_cases())
async def test_handlers(module, case, case_index, mock_resolver):
    module_name = module.__name__.split(".")[-1]
    input_url, expected_url = case
    log.debug(f"testing {module_name} handler case {case_index}, url:\n{input_url}")
    result = await handler_to_str(module.handler, input_url)
    if result:
        log.debug(f"handler path:\nhandlers/{module_name}.py")
    else:
        result = str(await convert(input_url))
    log.debug(f"pdsls url:\nhttps://pdsls.dev/{result}")
    # log.debug(f"test cases path:\n../test_cases/{module_name}.json")
    # log.debug(f"test cases path:\n../../test_cases/{module_name}.json")
    assert result == expected_url, (
        f"\nCase:     {module_name} {case_index}\n"
        f"Input:    {input_url}\n"
        f"Expected: {expected_url}\n"
        f"Actual:   {result}"
    )

def test_host_uniqueness():
    handlers_key = {}
    for module in modules:
        for host in module.hosts:
            assert host not in handlers_key
            handlers_key[host] = module.handler
