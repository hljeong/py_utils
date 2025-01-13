import functools


class ParametrizedMeta(type):
    def __getitem__(cls, parameter):
        return cls.of(parameter)

    @staticmethod
    def of(parameter):
        raise NotImplementedError


class Parametrized(metaclass=ParametrizedMeta):
    pass


class ParametrizedFunc:
    def __init__(self, func, parameter_name=None):
        self.func = func
        self.parameter_name = parameter_name

    def __call__(self, *a, **kw):
        return self.func(*a, **kw)

    def __getitem__(self, parameter):
        if self.parameter_name is None:
            return functools.partial(self.func, parameter)
        else:
            return functools.partial(self.func, **{self.parameter_name: parameter})


# todo: parametrize methods
def parametrize(func):
    return ParametrizedFunc(func)


def named_parametrize(parameter_name):
    def decorator(func):
        return ParametrizedFunc(func, parameter_name=parameter_name)

    return decorator
