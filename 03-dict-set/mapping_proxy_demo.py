import collections
from types import MappingProxyType


class StrKeyDict(collections.UserDict):  # <1>
    """UserDict的源码请见: /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/collections/__init__.py
    或：https://github.com/python/cpython/blob/9a28400aace26597b35950ac561d49c102b6daf4/Lib/collections/__init__.py#L994"""

    def __init__(self, *args, **kwargs):
        super(StrKeyDict, self).__init__(*args, **kwargs)
        self.data = MappingProxyType(self.data)  # 除了初始化时, 后续不能再修改

    def __missing__(self, key):  # <2>
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data  # <3>

    def __setitem__(self, key, item):
        self.data[str(key)] = item  # <4>


class Board:
    def __init__(self):
        self._pins = StrKeyDict({1: 'A', 'x': 'B', 2: 'C'})

    @property
    def pins(self):
        return self._pins


def test_pins():
    board = Board()
    print(board.pins['1'])
    print(board.pins['x'])
    try:
        board.pins[1] = 10  # 不可更改
    except TypeError:
        pass
    print(board.pins[2])
    print(board.pins[1])
    print(board.pins['1'])


if __name__ == '__main__':
    test_pins()
