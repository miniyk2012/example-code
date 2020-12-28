"""
Sentence: iterate over words using the Iterator Pattern, take #1

WARNING: the Iterator Pattern is much simpler in idiomatic Python;
see: sentence_gen*.py.
"""

# BEGIN SENTENCE_ITER
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # <1>
        return SentenceIterator(self.words)  # <2>


class SentenceIterator:

    def __init__(self, words):
        self.words = words  # <3>
        self.index = 0  # <4>

    def __next__(self):
        try:
            word = self.words[self.index]  # <5>
        except IndexError:
            raise StopIteration()  # <6>
        self.index += 1  # <7>
        return word  # <8>

    def __iter__(self):  # <9>
        return self


# END SENTENCE_ITER
class Sentence2:
    """极其不推荐的写法, 因为只能迭代一次.
    迭代器模式要求支持多种遍历, 同一个可迭代实例中获取多个独立的迭代器, 各个迭代器要维护自身的内部状态, 因此每次iter(my_iterable)
    都要新建一个独立的迭代器, 其实这是把迭代器和可迭代对象混淆了, 这样的实现是一个迭代器, 就是SentenceIterator"""

    def __init__(self, text):
        self.text = text
        self.index = 0
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # <1>
        return self

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word


def main():
    import sys
    import warnings
    try:
        filename = sys.argv[1]
        word_number = int(sys.argv[2])
    except (IndexError, ValueError):
        print('Usage: %s <file-name> <word-number>' % sys.argv[0])
        sys.exit(1)
    with open(filename, 'rt', encoding='utf-8') as text_file:
        s = Sentence(text_file.read())
    for n, word in enumerate(s, 1):
        if n == word_number:
            print(word)
            break
    else:
        warnings.warn('last word is #%d, "%s"' % (n, word))


if __name__ == '__main__':
    s2 = Sentence2('a b c')  # s2本质是是个迭代器(Iterator), 因此只能迭代一次
    print(list(s2))  # ['a', 'b', 'c']
    print(list(s2))  # [], s2只能迭代一次
    # main()

    s1 = Sentence('a b c')  # s1是可迭代对象
    for x in s1:
        print(x)
    for x in s1:
        print(x)
