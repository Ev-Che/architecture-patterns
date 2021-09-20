import time
from functools import wraps

from printer import Printer, ConsolePrinter


def simple_decorator(decorated_func):
    """Decorator designed to measure the execution
    time of the decorated_func

    @ wraps copies all info about the wrapped func
    and show this info in tracebacks.
    """

    @wraps(decorated_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        decorated_func(*args, **kwargs)
        stop = time.time()
        print(f'Total executing time: {stop - start}s')
    return wrapper


def decorator_with_args(printer_cls: Printer):
    """Decorator that can receive args"""
    def decorator_maker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            stop = time.time()
            printer_cls.print(f'Total executing time: {stop - start}s')

        return wrapper
    return decorator_maker


@decorator_with_args(ConsolePrinter)
def foo(*args):
    print(f'decorated function with args: {args}')


if __name__ == '__main__':
    foo(1, 2, 3, 4, 5)
