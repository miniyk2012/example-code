def paste_command():
    print('paste')


def open_command():
    print('open')


class MacroCommand:
    def __init__(self, cmds):
        self.cmds = list(cmds)

    def __call__(self):
        print('this is macro')
        for cmd in self.cmds:
            cmd()


def invoke(cmd):
    cmd()


if __name__ == '__main__':
    macro_cmd = MacroCommand([paste_command, open_command])
    invoke(paste_command)
    invoke(open_command)
    invoke(macro_cmd)
