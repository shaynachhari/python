import time
from functools import lru_cache

# lru_cache() is used to cache a function.
# it takes a argument maxsize which represents that for how many arguments we want function caching.


@lru_cache(maxsize=2)
def work(n):
    time.sleep(n)
    return "I am work function"


if __name__ == '__main__':
    print("Running work function")
    work(3)
    print(work(3))
    print(work(3))
    print(work(4))
    print(work(4))
    print(work(5))
    print(work(5))
    print(work(6))
    print(work(6))