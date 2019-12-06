class MySeq:
    def __getitem__(self, index):
        return index


class MyTry:

    def __init__(self, num):
        self._items = list(range(num))

    def __getitem__(self, index):
        return self._items[index]


if __name__ == '__main__':
    seq = MySeq()
    print(seq[1:4])
    print(seq[1:2:4])

    print([1, 2, 3, 4][slice(0, 3)])

    print(slice(None, 10, 2).indices(5))
    print(slice(-3, None, None).indices(5))
    print(type(slice(None, 10, 2).indices(5)))
    s = 'ABCDE'
    print(s[slice(None, 10, 2)])


    myTry = MyTry(10)
    myTry2 = MyTry(10)
    for a,b in zip(myTry, myTry2):
        print(a, b)
