import io
import tkinter
from frenchdeckx import FrenchDeck2


def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))


if __name__ == '__main__':
    print_mro(bool)
    print_mro(io.BytesIO)
    print_mro(io.TextIOWrapper)
    print_mro(FrenchDeck2)

    print_mro(tkinter.Text)
    print_mro(tkinter.Button)