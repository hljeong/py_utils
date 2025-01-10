def self_aware_repr(self, obj):
    return "self" if obj is self else repr(obj)


# todo: should this be in some other util lib? e.g. traits.py
def hashable(obj):
    try:
        hash(obj)
        return True

    except:
        return False


class CmpDict:
    def __init__(self, cmp):
        self.cmp = cmp
        self.l = list()

    def __repr__(self):
        # todo: represent self.cmp
        return f"CmpDict{{{', '.join(f'{self_aware_repr(self, k)}: {self_aware_repr(self, self[k])}' for k in self)}}}"

    # todo: how to deal with cmp?
    # def __eq__(self, rhs):

    def __iter__(self):
        return iter(k for k, _ in self.l)

    def __len__(self):
        return len(self.l)

    def __contains__(self, k):
        return any(self.cmp(k_, k) for k_, _ in self.l)

    def __getitem__(self, k):
        if k not in self:
            raise KeyError(k)

        return next((v for k_, v in self.l if self.cmp(k_, k)))

    def __setitem__(self, k, v):
        if k in self:
            for i, (k_, _) in enumerate(self.l):
                if self.cmp(k_, k):
                    self.l[i] = (k, v)
                    return

        else:
            self.l.append((k, v))

    def __delitem__(self, k):
        if k not in self:
            raise KeyError(k)

        self.l = list((k_, v) for k_, v in self.l if not self.cmp(k, v))


class EqDict:
    def __init__(self):
        self.d = dict()
        self.cd = CmpDict(lambda lhs, rhs: lhs == rhs)

    # todo: common superclass for all dicts? to reduce duplicate implementations
    def __repr__(self):
        # todo: represent self.cmp
        return f"EqDict{{{', '.join(f'{self_aware_repr(self, k)}: {self_aware_repr(self, self[k])}' for k in self)}}}"

    # todo: does type matter?
    def __eq__(self, rhs):
        return (
            isinstance(rhs, EqDict)
            and all(k in rhs for k in self)
            and all(k in self for k in rhs)
            and all(self[k] == rhs[k] for k in self)
        )

    # todo: maintain insertion order, by subclassing CompoundDict? which would maintain a separate insertion order list
    def __iter__(self):
        for k in self.d:
            yield k

        for k in self.cd:
            yield k

    def _d(self, k):
        return self.d if hashable(k) else self.cd

    def __len__(self):
        return len(self.d) + len(self.cd)

    def __contains__(self, k):
        return k in self._d(k)

    def __getitem__(self, k):
        return self._d(k)[k]

    def __setitem__(self, k, v):
        self._d(k)[k] = v

    def __delitem__(self, k):
        del self._d(k)[k]


class IdDict(CmpDict):
    def __init__(self):
        super().__init__(lambda lhs, rhs: lhs is rhs)
