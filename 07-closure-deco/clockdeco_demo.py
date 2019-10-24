# clockdeco_demo.py

import time

from clockdeco import clock


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    """阶乘函数"""
    return 1 if n < 2 else n * factorial(n - 1)


@clock
def foo(a, *, b=100, **kwargs):
    return a + b + sum(kwargs.values())


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print(factorial.__name__)
    print(factorial.__doc__)
    foo(10, c=10, d=15, b=12)
