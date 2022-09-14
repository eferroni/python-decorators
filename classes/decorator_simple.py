import types
from functools import wraps


class SimpleDecorator:

    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        print(f'Calling {self.func.__name__}')
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@SimpleDecorator
def simple_function():
    print('Hello!')


if __name__ == '__main__':
    simple_function()