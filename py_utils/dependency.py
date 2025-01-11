from .natural_language import this_many
from .sentinel import Sentinel


class MissingDependencies(Sentinel):
    def __new__(cls, *missing_dependencies):
        assert len(missing_dependencies) > 0
        # not exactly possible to get the names of the missing dependencies...
        return super().__new__(
            cls,
            f"this object is missing {this_many(len(missing_dependencies), 'dependency')}",
        )


def requires(*dependencies):
    missing_dependencies = [
        dependency for dependency in dependencies if dependency is None
    ]

    return lambda target: (
        MissingDependencies(missing_dependencies)
        if len(missing_dependencies) > 0
        else target
    )
