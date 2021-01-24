"""
A coroutine to compute a running average.

Testing ``averager`` by itself::

    >>> coro_avg = averager()
    >>> next(coro_avg)
    >>> coro_avg.send(10)
    >>> coro_avg.send(30)
    >>> coro_avg.send(6.5)
    >>> coro_avg.send(None)
    Traceback (most recent call last):
       ...
    StopIteration: Result(count=3, average=15.5)


Driving it with ``yield from``::

    >>> def summarize(results):
    ...     while True:
    ...         result = yield from averager()
    ...         results.append(result)
    ...
    >>> results = []
    >>> summary = summarize(results)
    >>> next(summary)
    >>> for height in data['girls;m']:
    ...     summary.send(height)
    ...
    >>> summary.send(None)
    >>> for height in data['boys;m']:
    ...     summary.send(height)
    ...
    >>> summary.send(None)
    >>> results == [
    ...     Result(count=10, average=1.4279999999999997),
    ...     Result(count=9, average=1.3888888888888888)
    ... ]
    True

"""

# BEGIN YIELD_FROM_AVERAGER
from collections import namedtuple

from coroutil import coroutine  # <4>

Result = namedtuple('Result', 'count average')
averager_total_count = 0
group_total_count = 0

# the subgenerator
def averager():  # <1>
    global averager_total_count
    averager_total_count += 1
    print('新建averager', averager_total_count)
    total = 0.0
    count = 0
    average = None
    output = None
    while True:
        if output is None:
            output = 10
            term = yield 'first'  # <2>
        else:
            term = yield output
        if term is None:  # <3>
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)  # <4>


# the delegating generator
def grouper(results, key):  # <5>
    global group_total_count
    group_total_count += 1
    print('新建group', group_total_count)
    while True:  # <6>
        a = yield from averager()  # <7>
        results[key] = a


    # the client code, a.k.a. the caller
def main(data):  # <8>
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # <9>
        print('预激:', next(group))  # <10>  # 这个next会透过group到averager上, 在averager的yield处暂停住
        for value in values:
            print(group.send(value))  # <11>
        last = group.send(None)  # important! <12>
        # 非常微妙的一步, result[key]被赋值后, 由于grouper的while循环, 还会新建一个averager并走到yield处停住, 然后控制权交给main函数,
        # main函数这里直接又for循环新建group了, 原来的那个协程后续就被垃圾回收了
        print('last:', last)
        print()

    # print(results)  # uncomment to debug
    report(results)


# output report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data)

# END YIELD_FROM_AVERAGER
