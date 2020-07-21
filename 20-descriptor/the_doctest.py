def m():
    try:
        m.s += 1
    except AttributeError:
        m.s = 0

    s = m.s

    def a():
        print(s)  # 闭包

    return a


if __name__ == '__main__':
    z1 = m()
    z1()

    z2 = m()
    z2()
    z1()
