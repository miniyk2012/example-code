""" Example adapted from ``yield_delegate_fail.py``

The following program performs a simple abstraction over the process of
yielding.

"""
import time


# BEGIN YIELD_DELEGATE_FIX
def f():
    def do_yield(n):
        yield n

    x = 0
    while True:
        time.sleep(0.5)
        x += 1
        yield from do_yield(x)
        # for n in do_yield(x):
        #     yield n


# END YIELD_DELEGATE_FIX

if __name__ == '__main__':
    print('Invoking f() now produces a generator')
    g = f()
    print(next(g))
    print(next(g))
    print(next(g))
