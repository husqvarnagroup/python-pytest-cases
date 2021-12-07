from makefun import wraps

from pytest_cases.fixture_core1_unions import is_used_request, NOT_USED


def ignore_unused_generate_asyncgen_wrapped_fixture_func(fixture_func, new_sig, func_needs_request):
    # async generator function (with a yield statement)
    @wraps(fixture_func, new_sig=new_sig)
    async def wrapped_fixture_func(*args, **kwargs):
        request = kwargs['request'] if func_needs_request else kwargs.pop('request')
        if is_used_request(request):
            async for res in fixture_func(*args, **kwargs):
                yield res
        else:
            yield NOT_USED

    return wrapped_fixture_func


def decorate_fixture_plus_asyncgen_wrapped_fixture_func(fixture_func, new_sig, _map_arguments):
    # async generator function (with a yield statement)
    @wraps(fixture_func, new_sig=new_sig)
    async def wrapped_fixture_func(*_args, **_kwargs):
        if not is_used_request(_kwargs['request']):
            yield NOT_USED
        else:
            _args, _kwargs = _map_arguments(*_args, **_kwargs)
            async for res in fixture_func(*_args, **_kwargs):
                yield res
