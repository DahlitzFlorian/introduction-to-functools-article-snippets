# wraps.py

from functools import wraps


def show_args(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"Calling function {f.__name__} with {args} and {kwargs}")
        return f(*args, **kwargs)
    return wrapper


@show_args
def add(a: int, b: int) -> int:
    """Add two numbers a and b and return the result"""
    return a + b


print(add(5, 1))
print(add.__doc__)
print(add.__name__)
