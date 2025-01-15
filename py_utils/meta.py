def meta(repr=None):
    d = dict()

    if repr is not None:
        d["__repr__"] = lambda _: repr

    return type("meta", (type,), d)
