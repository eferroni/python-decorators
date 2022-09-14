from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def printer():
    print('func')


if __name__ == '__main__':
    printer()
