import time

lambda_func = lambda a, b: a + b


def func(a):
    return a


class A:
    def __call__(self):
        pass

    def method(self):
        pass


def generator_func():
    yield 5


# x是可调用对象: 指可以将调用运算符(即())应用到x上面
assert callable(A)
assert callable(lambda_func)
assert callable(func)
assert callable(A())
assert callable(A().method)
assert callable(generator_func)
assert callable(dict.get)
assert callable(time.strftime)

assert not callable(A().method())
assert not callable(lambda_func(1, 2))
assert not callable(generator_func())
