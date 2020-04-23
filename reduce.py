# reduce.py

from functools import reduce
from operator import add

iterable = [1, 2, 3, 4, 5]
result = reduce(add, iterable)
print(result)
