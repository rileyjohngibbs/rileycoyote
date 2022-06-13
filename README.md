# Riley Coyote

My plan is to overengineer some Python stuff here.

## abstractattribute

Use this to define attributes that raise `NotImplementedError` when accessed.

Example usage:

```python
class Foo:
    attr: int = abstractattribute(int)

class Bar(Foo):
    attr = 5

Bar.attr  # 5
Foo.attr  # NotImplementedError
```

But mostly this is important for use with Abstract Config Classes (`ACC`), which will enforce that subclasses (re)define the abstractattributes.

Example usage:

```python
class Foo(ACC):
    attr: int = abstractattribute(int)

# Raises TypeError because `attr` is not defined
class Bar(Foo):
    pass
```