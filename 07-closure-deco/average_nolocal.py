from operator import attrgetter


def make_average():
    count, total = 0, 0

    def avg(val):
        nonlocal count, total
        count += 1
        total += val
        return total / count

    return avg


if __name__ == '__main__':
    avg = make_average()
    print(avg(10))
    print(avg(20))

    avg2 = make_average()
    print(avg2(10))

    print(avg(30))

    print(avg.__code__.co_freevars)
    print('avg', list(map(attrgetter('cell_contents'), avg.__closure__)))
    print('avg2', list(map(attrgetter('cell_contents'), avg2.__closure__)))
