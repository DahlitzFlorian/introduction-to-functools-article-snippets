# lru_cache_static_website_content.py

from functools import lru_cache
from urllib import error
from urllib import request


@lru_cache(maxsize=32)
def get_pep(number: int) -> str:
    resource = f"http://www.python.org/dev/peps/pep-{number:04d}/"
    print(resource)
    try:
        with request.urlopen(resource) as s:
            return s.read()
    except error.HTTPError:
        return "Not Found"


list_of_peps = [8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991]

for n in list_of_peps:
    pep = get_pep(n)
    print(n, len(pep))

print(get_pep.cache_info())
