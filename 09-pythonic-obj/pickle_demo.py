import pickle
import time


class Slate:
    '''Class to store a string and a changelog, and forget its value when
    pickled.'''

    def __init__(self, value):
        self.value = value
        self.last_change = time.asctime()
        self.history = {}

    def change(self, new_value):
        time.sleep(1.1)
        # Change the value. Commit last value to history
        self.history[self.last_change] = self.value
        self.value = new_value
        self.last_change = time.asctime()

    def print_changes(self):
        print('Changelog for Slate object:', self.history)
        if not self.history:
            return
        for k, v in self.history.items():
            print('%s\t %s' % (k, v))

    def __getstate__(self):
        # Deliberately do not return self.value or self.last_change.
        # We want to have a "blank slate" when we unpickle.
        # 你可以自定义当对象被序列化时返回的状态，而不是使用 __dict__ 方法，当逆序列化对象的时候，返回的状态将会被 __setstate__ 方法调用。
        return self.last_change

    def __setstate__(self, state):
        # Make self.last_change = state and history and value None
        # 在对象逆序列化的时候，如果 __setstate__ 定义过的话，对象的状态将被传给它而不是传给 __dict__ 。
        # 这个方法是和 __getstate__ 配对的，当这两个方法都被定义的时候，你就可以完全控制整个序列化与逆序列化的过程了。
        self.last_change = state
        self.history, self.value = None, None


if __name__ == '__main__':
    slate = Slate(0)
    slate.change(1)
    slate.change(2)
    slate.change(3)
    slate.print_changes()
    print(slate.value)
    print(slate.last_change)
    print(slate.__dict__)

    print()
    store = pickle.dumps(slate)
    print(store)
    new_slate = pickle.loads(store)
    new_slate.print_changes()
    print(new_slate.value)
    print(new_slate.last_change)
    print(new_slate.history)
