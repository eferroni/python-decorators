from functools import wraps
import logging


def logger(level, name=None, msg=None):
    def decorate(func):
        log_name = name if name else func.__name__
        log_msg = msg if msg else func.__name__

        logging.basicConfig(filename=f'{func.__name__}.log', level=logging.DEBUG)
        log = logging.getLogger(log_name)

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            log.log(level, f"{args} = {str(result)}")
            return result
        return wrapper
    return decorate


@logger(logging.DEBUG)
def counter(a, b):
    return a + b


if __name__ == '__main__':
    counter(1, 2)
