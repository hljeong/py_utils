# todo: flesh this out, see pep 661: https://peps.python.org/pep-0661/
class Sentinel:
    _sentinels = dict()

    def __new__(cls, name):
        sentinel = super().__new__(cls)
        sentinel._repr = name  # type: ignore
        return Sentinel._sentinels.setdefault(name, sentinel)

    def __repr__(self):
        return self._repr  # type: ignore
