import pytest
import pytest_asyncio

import pytest_cases
from pytest_cases import parametrize_with_cases

pytestmark = pytest.mark.asyncio


@pytest_cases.fixture
async def fixture_async_gen():
    yield "fixture_async_gen"


@pytest_cases.fixture
def fixture_gen():
    yield "fixture_gen"


@pytest_cases.fixture
async def fixture_async():
    return "fixture_async"


@pytest_cases.fixture
def fixture():
    return "fixture"


@pytest_cases.fixture
def fixture_assert(fixture, fixture_async, fixture_gen, fixture_async_gen, request):
    assert fixture == "fixture"
    assert fixture_async == "fixture_async"
    assert fixture_gen == "fixture_gen"
    assert fixture_async_gen == "fixture_async_gen"

    return "assert"


def case_1(fixture_assert):
    return "ok"


def case_2():
    return "ok"


@parametrize_with_cases("case", cases=".", prefix="case_")
async def test_cases(case):
    assert case == "ok"
