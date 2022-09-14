from functools import wraps


def simple_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


@simple_decorator
def simple_function():
    print('Hello!')


if __name__ == '__main__':
    simple_function()

