import itertools
import operator

if __name__ == '__main__':
    print(list(itertools.islice(itertools.count(0, 0.1), 3)))
    cy = itertools.cycle('ABC')
    print(next(cy))
    print(list(itertools.islice(cy, 1, 10)))
    rp = itertools.repeat(7)
    print(next(rp), next(rp))
    print(list(itertools.repeat('AB', 3)))
    print(list(map(operator.mul, range(11), itertools.repeat(5))))

    print('组合学生成器')
    print(list(itertools.combinations('ABC', 2)))
    print(list(itertools.combinations_with_replacement('ABC', 2)))
    print(list(itertools.permutations('ABC', 2)))
    print(list(itertools.product('ABC', repeat=2)))
