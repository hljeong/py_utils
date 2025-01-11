from .dependency import requires

try:
    import pytest
except:
    pytest = None


@requires(pytest)
def parametrize(argnames, argvalues, *a, **kw):
    kw.setdefault("ids", list(map(str, argvalues)))
    return pytest.mark.parametrize(argnames, argvalues, *a, **kw)  # type: ignore
