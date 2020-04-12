from random import randrange

from tombola import Tombola
import abc

@Tombola.register  # <1>
class TomboList(list):  # <2>

    def pick(self):
        if self:  # <3>
            position = randrange(len(self))
            return self.pop(position)  # <4>
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # <5>

    def loaded(self):
        return bool(self)  # <6>

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList)  # <7>


if __name__ == '__main__':
    print(issubclass(TomboList, Tombola))
    t = TomboList(range(100))
    print(isinstance(t, Tombola))
    print(TomboList.__mro__)
    print(t.loaded())
    print(Tombola.__subclasses__())