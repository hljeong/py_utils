# todo: flesh this out, see pep 661: https://peps.python.org/pep-0661/
class Sentinel:
    _sentinels = dict()

    def __init__(self, name):
        self.name = name

    def __new__(cls, name):
        sentinel = super().__new__(cls)
        return Sentinel._sentinels.setdefault(name, sentinel)

    def __repr__(self):
        return self.name

    def __copy__(self):
        return Sentinel._sentinels[self.name]

    def __deepcopy__(self, _):
        return self.__copy__()
