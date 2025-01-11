from .dependency import requires

try:
    import pytest
except:
    pytest = None


class Parameters(tuple):
    def __new__(cls, description, *argvalues):
        assert isinstance(description, str)
        parameters = tuple.__new__(Parameters, argvalues)
        parameters._str = description  # type: ignore
        return parameters

    def __str__(self):
        return self._str  # type: ignore


@requires(pytest)
def parametrize(argnames, argvalues, *a, **kw):
    def stupid_quirk(argvalue):
        if isinstance(argvalue, Parameters) and len(argvalue) == 1:
            return argvalue[0]
        return argvalue

    kw.setdefault("ids", list(map(str, argvalues)))
    return pytest.mark.parametrize(argnames, list(map(stupid_quirk, argvalues)), *a, **kw)  # type: ignore
