from functools import reduce
from typing import Any, Generic, TypeVar


T_ = TypeVar("T_")


class _abstractattribute(Generic[T_]):
    def __init__(self, type_: type[T_]):
        self.type_ = type_

    def __get__(self, *_) -> T_:
        raise NotImplementedError()

    def __set__(self, *_) -> None:
        raise NotImplementedError()


def abstractattribute(type_: type[T_]) -> T_:
    return type(
        f"abstractattribute_{type_.__name__}",
        (_abstractattribute,),
        {"__isabstractmethod__": True},
    )(type_)


class ACCMeta(type):
    def __new__(cls, name: str, bases: tuple[type], attrs: dict[str, Any]):
        inherited_abstractions: set[str] = reduce(
            lambda attrs, base: {attr for attr in attrs.difference(base.__dict__)}
            | {
                attr
                for attr, value in base.__dict__.items()
                if getattr(value, "__isabstractmethod__", False)
            },
            reversed(bases),
            set(),
        )
        unresolved_abstractions = inherited_abstractions.difference(attrs)
        if unresolved_abstractions:
            raise TypeError(f"{name} must define values for: {unresolved_abstractions}")
        return super().__new__(cls, name, bases, attrs)


class ACC(metaclass=ACCMeta):
    pass
