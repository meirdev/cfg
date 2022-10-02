import inspect
from abc import abstractmethod
from typing import Callable, ParamSpec, Protocol, TypeVar

from .predicates import unix, windows


class SupportsBool(Protocol):
    @abstractmethod
    def __bool__(self) -> int:
        pass


class CfgNameError(NameError):
    pass


def _raise_name_error(name: str):
    def inner(*args, **kwargs):
        raise CfgNameError(f"name '{name}' is not defined")

    return inner


P = ParamSpec("P")
T = TypeVar("T")


def cfg(condition: SupportsBool):
    def inner(function: Callable[P, T]) -> Callable[P, T]:
        if condition:
            return function

        module = inspect.getmodule(function)
        if function.__name__ in module.__dict__:
            return module.__dict__[function.__name__]

        return _raise_name_error(function.__name__)

    return inner


__all__ = [
    "cfg",
    "unix",
    "windows",
]
