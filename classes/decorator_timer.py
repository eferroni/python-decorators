from functools import wraps
import time
import types

class TimeThis:
    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.__wrapped__(*args, **kwargs)
        end = time.time()
        print(self.func.__name__, end-start)
        return result

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@TimeThis
def counter(size):
    for i in range(size):
        continue


if __name__ == '__main__':
    counter(10000)
    counter(1000000)
    counter(100000000)
