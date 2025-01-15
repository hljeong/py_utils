from types import new_class

from .parametrize import parametrize


# todo: is >1 bases ever unavoidable? i.e., needs to be supported?
@parametrize("base")
def Meta(*, repr=None, base=None):
    name = "Meta" if not base else f"Meta[{base.__name__}]"

    base = base or type

    kwds = dict()

    if repr is not None:
        kwds["__repr__"] = lambda _: repr

    # this is adding "Meta" to the wrong end... but it works
    return new_class(name, (base,), dict(metaclass=type(f"Meta{name}", (base,), kwds)))
