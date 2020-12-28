import itertools

if __name__ == '__main__':
    print(list(enumerate('ABC')))
    print(list(itertools.chain([1, 2, 3])))
    print(list(itertools.chain(enumerate('ABC'), range(2))))
    print(list(itertools.chain.from_iterable(enumerate('ABC'))))
    print(list(zip('ABC', range(5))))
    print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))

    print()
    suits = 'spades hearts diamonds clubs'.split()
    print(list(itertools.product('AK', suits)))
    rows = itertools.product('ABC', range(2), repeat=2)
    for row in rows:
        print(row)
