import collections
from random import shuffle


class Foo:
    def __getitem__(self, index):
        return range(0, 30, 10)[index]


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, key, value):
        self._cards[key] = value


def handle_foo():
    foo = Foo()
    print(foo[1])
    for v in foo:
        print(v)
    print(10 in foo)
    print(15 in foo)


def handle_deck():
    deck = FrenchDeck()
    print(len(deck))
    print(deck[:5])
    shuffle(deck)
    print(len(deck))
    print(deck[:5])


class Struggle:
    def __len__(self):
        return 23


def check_instance():
    print(isinstance(Struggle(), collections.Sized))


if __name__ == '__main__':
    # handle_deck()
    check_instance()
