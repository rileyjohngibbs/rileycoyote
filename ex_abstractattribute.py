from abstractattribute import abstractattribute


class Foo:
    X = abstractattribute(str)
    Y: int = abstractattribute(int)


class Bar(Foo):
    X = "a string"
    Y = 7


def get_x_from_foo(f: type[Foo]) -> str:
    return f.X


get_x_from_foo(Bar)
