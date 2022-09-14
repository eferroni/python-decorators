from functools import wraps
import logging
import types

class Logger:
    def __init__(self, level, name=None, msg=None):
        self.level = level
        self.name = name
        self.msg = msg

    def __call__(self, func):
        log_name = self.name if self.name else func.__name__
        log_msg = self.msg if self.msg else func.__name__

        logging.basicConfig(filename=f'{func.__name__}.log', level=logging.DEBUG)
        log = logging.getLogger(log_name)

        wraps(func)(self)

        def wrapper(*args, **kwargs):
            result = self.__wrapped__(*args, **kwargs)
            log.log(self.level, f"{args} = {str(result)}")
            return result
        return wrapper

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Logger(logging.WARNING)
def counter(a, b):
    return a + b


if __name__ == '__main__':
    counter(1, 5)
