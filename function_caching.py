import time
from functools import lru_cache


@lru_cache(maxsize=4)
def some_work(n):
    time.sleep(n)


if __name__ == '__main__':
    print('calling some_work...')
    some_work(3)
    some_work(4)
    some_work(2)
    some_work(1)
    print('Done... calling again')
    some_work(3)
    print('Done....')
