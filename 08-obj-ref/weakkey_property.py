from weakref import WeakKeyDictionary

a = None


class Grade:
    def __init__(self):
        self._value = WeakKeyDictionary()  # 防止内存泄露
        global a
        a = self

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._value.get(instance, None)

    def __set__(self, instance, value):
        self._value[instance] = value


class Exam:
    math_grade = Grade()


if __name__ == '__main__':
    exam1 = Exam()
    exam1.math_grade = 100

    exam2 = Exam()
    exam2.math_grade = 60

    print(exam1.math_grade)
    print(exam2.math_grade)

    print(list(a._value.items()))

    del exam1

    print(list(a._value.items()))
