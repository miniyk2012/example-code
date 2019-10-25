# clockdeco.py

import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        """统计时间"""
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ('{}={}'.format(key, repr(val)) for key, val in sorted(kwargs.items()))
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked
