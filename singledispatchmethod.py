# singledispatchmethod.py

from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg


neg = Negator()
print(neg.neg(5))
print(neg.neg(True))
print(neg.neg("Hello"))
