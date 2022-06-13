import pytest
from abc import abstractmethod

from abstractattribute import ACC, abstractattribute


@pytest.fixture
def base_class():
    class Foo:
        str_attr = abstractattribute(str)
        int_attr = abstractattribute(int)

    return Foo


def test_abstrattr_name(base_class):
    str_attr_name = base_class.__dict__["str_attr"].__class__.__name__
    assert str_attr_name == "abstractattribute_str"


def test_no_abstract_str_access(base_class):
    with pytest.raises(NotImplementedError):
        base_class.str_attr


def test_no_abstract_int_access(base_class):
    with pytest.raises(NotImplementedError):
        base_class.int_attr


def test_concrete_access(base_class):
    class Bar(base_class):
        str_attr = "hello"
        int_attr = 5

    assert Bar.str_attr == "hello"
    assert Bar.int_attr == 5


@pytest.fixture
def base_acc():
    class Foo(ACC):
        str_attr = abstractattribute(str)
        int_attr = abstractattribute(int)

    return Foo


def test_incomplete_implementation(base_acc):
    with pytest.raises(TypeError):

        class _(base_acc):
            pass


def test_skip_implementations(base_acc):
    class Bar(base_acc):
        str_attr = abstractattribute(str)
        int_attr = 5

    with pytest.raises(TypeError):

        class _(Bar):
            pass


def test_missing_method():
    class Foo(ACC):
        @classmethod
        @abstractmethod
        def one(cls) -> int:
            pass

    with pytest.raises(TypeError):

        class _(Foo):
            pass
