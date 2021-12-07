from makefun import wraps

from pytest_cases.fixture_core1_unions import is_used_request, NOT_USED


def ignore_unused_generate_async_wrapped_fixture_func(fixture_func, new_sig, func_needs_request):
    # coroutine function with return statement
    @wraps(fixture_func, new_sig=new_sig)
    async def wrapped_fixture_func(*args, **kwargs):
        request = kwargs['request'] if func_needs_request else kwargs.pop('request')
        if is_used_request(request):
            return await fixture_func(*args, **kwargs)
        else:
            return NOT_USED

    return wrapped_fixture_func


def decorate_fixture_plus_async_wrapped_fixture_func(fixture_func, new_sig, _map_arguments):
    # coroutine function with return statement
    @wraps(fixture_func, new_sig=new_sig)
    async def wrapped_fixture_func(*_args, **_kwargs):
        if not is_used_request(_kwargs['request']):
            return NOT_USED
        else:
            _args, _kwargs = _map_arguments(*_args, **_kwargs)
            return await fixture_func(*_args, **_kwargs)
