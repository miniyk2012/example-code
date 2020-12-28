import collections


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class AnswerDict(dict):
    def __getitem__(self, key):
        return 42


def useless():
    dd = DoppelDict(one=1)
    print(dd)
    dd['two'] = 2
    dd.update(three=3)
    print(dd)

    ad = AnswerDict(a='foo')
    print(ad)
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)


class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42


def useful():
    dd = DoppelDict2(one=1)
    print(dd)
    dd['two'] = 2
    dd.update(three=3)
    print(dd)

    ad = AnswerDict2(a='foo')
    print(ad)
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)


if __name__ == '__main__':
    useful()
