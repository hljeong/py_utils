from .dependency import requires

try:
    import pytest
except:
    pytest = None


@requires(pytest)
def parametrize(argnames, argvalues, *a, **kw):
    kw.setdefault("ids", list(map(str, argvalues)))
    return pytest.mark.parametrize(argnames, argvalues, *a, **kw)  # type: ignore


class Parameters(tuple):
    def __new__(cls, description, *argvalues):
        assert isinstance(description, str)
        parameters = tuple.__new__(Parameters, argvalues)
        parameters._str = description  # type: ignore
        return parameters

    def __str__(self):
        return self._str  # type: ignore
