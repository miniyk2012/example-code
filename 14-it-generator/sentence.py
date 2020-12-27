"""
Sentence: access words by index
"""
import re
import reprlib
from collections import abc

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # <1>

    def __getitem__(self, index):
        return self.words[index]  # <2>

    def __len__(self):  # <3>
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # <4>


if __name__ == '__main__':
    s = Sentence("hello world")
    for w in s:
        print(w)

    print(isinstance(s, abc.Iterable))


    class Foo:
        def __iter__(self):
            pass


    print(isinstance(Foo(), abc.Iterable))

    it = iter(s)
    print(next(it))

    it2 = iter(it)
    print(next(it2))