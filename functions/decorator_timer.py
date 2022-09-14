from functools import wraps
import time


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@time_this
def counter(size):
    for i in range(size):
        continue


if __name__ == '__main__':
    counter(10000)
    counter(1000000)
    counter(100000000)
