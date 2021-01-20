import inspect
from collections.abc import Iterable
from functools import wraps


def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""

    @wraps(func)
    def primer(*args, **kwargs):  # <1>
        gen = func(*args, **kwargs)  # <2>
        next(gen)  # <3>
        return gen  # <4>

    return primer


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)


def simple_coro2(a):
    print('-> Started: a=', a)
    b = yield a
    print('-> Received: b=', b)
    c = yield a + b
    print('-> Received: c=', c)


def coro1_test():
    my_coro = simple_coroutine()
    print(my_coro)
    print(inspect.getgeneratorstate(my_coro))
    print(next(my_coro))
    print(inspect.getgeneratorstate(my_coro))
    try:
        my_coro.send(42)
    except StopIteration:
        print(inspect.getgeneratorstate(my_coro))


def coro2_test():
    coro2 = simple_coro2(14)
    print(inspect.getgeneratorstate(coro2))
    print(next(coro2))
    print(inspect.getgeneratorstate(coro2))
    print(coro2.send(28))
    try:
        print(inspect.getgeneratorstate(coro2))
        coro2.send(99)
    except StopIteration:
        print(inspect.getgeneratorstate(coro2))


@coroutine
def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


def cal_average():
    coro_avg = averager()
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))


def coro_exception():
    coro_avg = averager()
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))
    try:
        print(coro_avg.send('spam'))
    except TypeError as e:
        print(e)
    coro_avg.send(60)


def gen():
    yield from 'AB'
    yield from range(1, 3)


def chain(*iterables):
    for ele in iterables:
        yield from ele


def flatten(items, ignore_types=(str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and type(item) not in ignore_types:
            yield from flatten(item)
        else:
            yield item


if __name__ == '__main__':
    coro1_test()
    print()
    coro2_test()
    print()
    cal_average()
    # print()
    # coro_exception()
    print()
    print(list(gen()))
    print()
    print(list(chain('ABC', range(3))))

    print()
    items = [1, 2, [3, 4, [5, 6], 7, ['Dave', 'Paula', ['Thomas', 'Lewis']]], 8]
    result = []
    f = flatten(items)
    while True:
        try:
            result.append(f.send(None))
        except StopIteration:
            break
    print(result)
    print(list(flatten(items)))
