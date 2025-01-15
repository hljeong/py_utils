from types import new_class


def meta(**kwds):
    def decorator(cls):
        return new_class(
            cls.__name__,
            cls.__bases__,
            dict(metaclass=type("Meta", (cls.__class__,), kwds)),
            lambda ns: ns.update(cls.__dict__),
        )

    return decorator
