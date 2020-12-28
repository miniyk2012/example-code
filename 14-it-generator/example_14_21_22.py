import itertools
import threading


def generator():
    for i in range(10 ** 6):
        yield i


def tee_multithreading():
    """tee不是线程安全的"""
    g = generator()
    g1, g2 = itertools.tee(g)
    for x in [g1, g2]:
        threading.Thread(target=sum, args=(x,)).start()


if __name__ == '__main__':
    print(list(itertools.groupby('LLLGGAA')))
    for char, group in itertools.groupby('LLLGGAA'):
        print(char, '->', list(group))
    print()
    animals = ['duck', 'eagle', 'bear', 'rat', 'giraffe', 'bat', 'dolphin', 'shark', 'lion']
    animals.sort(key=len)
    for length, group in itertools.groupby(animals, len):
        print(length, '->', list(group))

    print()
    print(list(reversed(animals)))
    for length, group in itertools.groupby(reversed(animals), len):
        print(length, '->', list(group))

    print(list(itertools.tee('ABC')))
    g1, g2 = itertools.tee('ABC')
    print(next(g1))
    print(next(g2))
    print(next(g2))
    print(list(g1))
    print(list(g2))
    print(list(zip(*itertools.tee('ABC'))))

    # tee_multithreading()

    g = (n for n in [0, 0.0, 7, 8])
    print(any(g))
    print(next(g))
    print(sorted(itertools.islice(itertools.count(0, -1), 10)))
