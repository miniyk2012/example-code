import inspect


def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))

    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s %s/>' % (name, attr_str)


def f(a, *, b=10, **kwargs):
    pass


def f2(a, *args, b=12, **kwargs):
    pass


if __name__ == '__main__':
    print(tag("div", "hello", "yangkai", id="3", cls="alert"))
    print(tag("div", "hello", "yangkai", id="3"))
    print(tag("div", cls="alert"))

    f(1, b=3)  # 不想有数量不定的位置参数
    f2(1, 2, b=21)

    sig = inspect.signature(tag)
    my_tag = dict(name="div", title="hello", id="3", cls="alert")

    bound_args = sig.bind(**my_tag)
    print(bound_args)

    del my_tag['name']
    try:
        bound_args = sig.bind(**my_tag)
    except TypeError as e:
        assert e.args[0] == "missing a required argument: 'name'"

    print("*" * 50)
    from functools import partial

    picture = partial(tag, 'img', 'sfda', cls='pic-frame')
    print(picture('ejf', src='wumpus.jpeg'))
    print(picture)
    print(picture.func)
    print(picture.keywords)
    print(picture.args)
