from abstractattribute import ACC, abstractattribute


class Foo:
    X = abstractattribute(str)
    Y: int = abstractattribute(int)


class Bar(Foo):
    X = "a string"
    Y = 7


def get_x_from_foo(f: type[Foo]) -> str:
    """Type checks correctly."""
    return f.X


get_x_from_foo(Bar)


class FooAbstract(ACC):
    X = abstractattribute(str)
    Y = abstractattribute(int)


try:
    class BarIncomplete(FooAbstract):
        pass
except TypeError:
    pass


class BarComplete(FooAbstract):
    X = "five"
    Y = 5