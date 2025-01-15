from types import new_class, prepare_class


def meta(**kwds):
    def decorator(cls):
        # roundabout way to get the most derived metaclass of superclasses of the decorated class...
        meta = prepare_class("", cls.__bases__)[0]
        return new_class(
            cls.__name__,
            cls.__bases__,
            dict(metaclass=type("Meta", (meta,), kwds)),
            lambda ns: ns.update(cls.__dict__),
        )

    return decorator
