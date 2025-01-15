from functools import partial, update_wrapper
from inspect import isgenerator


class ParametrizedMeta(type):
    def __getitem__(cls, parameter):
        if isgenerator(parameter):
            parameter = tuple(parameter)
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
        update_wrapper(self, self.func)

    def __repr__(self):
        return f"parametrized {self.func!r}"

    def __call__(self, *a, **kw):
        return self.func(*a, **kw)

    def __getitem__(self, parameter):
        if self.parameter_name is None:
            wrapped = update_wrapper(partial(self.func, parameter), self.func)
        else:
            wrapped = update_wrapper(
                partial(self.func, **{self.parameter_name: parameter}), self.func
            )
        wrapped.__name__ += f"[{parameter}]"
        return wrapped

    def __get__(self, instance, _):
        return ParametrizedFunc(
            update_wrapper(partial(self.func, instance), self.func),
            parameter_name=self.parameter_name,
        )


# must use @parametrize() for parametrizing first arg
# hard to get type checking to work otherwise
def parametrize(parameter_name=None):
    return lambda func: ParametrizedFunc(func, parameter_name=parameter_name)
