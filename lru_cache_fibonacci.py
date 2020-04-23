# lru_cache_fibonacci.py

from functools import lru_cache
from timeit import timeit


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


list_of_fib_numbers = [fib(n) for n in range(16)]
print(list_of_fib_numbers)
print(fib.cache_info())
