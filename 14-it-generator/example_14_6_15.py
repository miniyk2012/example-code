import operator
from itertools import accumulate, starmap


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


if __name__ == '__main__':
    for c in gen_AB():
        print('-->', c)

    print()
    for c in iter(gen_AB()):
        print('-->', c)

    print()
    print(list(accumulate(range(1, 11), operator.mul)))
    print(list(enumerate('abcdedf', 1)))
    print(list(map(operator.mul, range(11), range(8))))
    print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))
    print(list(starmap(pow, [(2, 5), (3, 2), (10, 3)])))
    print(list(starmap(operator.mul, enumerate('abc', 1))))
