from types import new_class


# todo: breaks type checker -- possible to fix?
def meta(**kwds):
    def decorator(cls):
        return new_class(
            cls.__name__,
            cls.__bases__,
            dict(metaclass=type("Meta", (cls.__class__,), kwds)),
            lambda ns: ns.update(cls.__dict__),
        )

    return decorator


# todo: make named
def subclass_of(*classes):
    class Subclass(*classes):
        pass

    return Subclass


# todo: make named, is there a better name for "submetaclass"?
# returns a class whose metaclass is the subclass of all
# metaclasses of the given list of classes
def submetaclass_of(*classes):
    metaclasses = {type}
    for base in classes:
        metaclasses = set(
            filter(
                lambda metaclass: not issubclass(base.__class__, metaclass), metaclasses
            )
        )
        metaclasses.add(base.__class__)

    class SubMetaclass(metaclass=subclass_of(*metaclasses)):
        pass

    return SubMetaclass
