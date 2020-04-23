# total_ordering.py

from functools import total_ordering


@total_ordering
class Pythonista:
    firstname: str
    lastname: str

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pythonista):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other: object):
        if not isinstance(other, Pythonista):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))


guido = Pythonista("Guido", "van Rossum")
brett = Pythonista("Brett", "Cannon")
print(guido < brett)
