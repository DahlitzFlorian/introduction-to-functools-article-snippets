# singledispatch.py

from functools import singledispatch


@singledispatch
def mul(a, b):
    if type(a) is not type(b):
        return NotImplemented
    return a * b


@mul.register
def _(a: str, b: str):
    return a + b


print(mul(1, 2))
print(mul(1.5, 2.5))
print(mul("1", "2"))
print(mul(1, 1.0))
