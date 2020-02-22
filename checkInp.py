import sys

def getch_noTimeout():
    ''' Wait for a key press on the console and return it. '''
    result = None
    import termios
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    try:
        result = sys.stdin.read(1)
    except IOError:
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    """Fetch and character using the termios module."""
    def __init__(self):
        import tty, sys
        from select import select

    def __call__(self,timeout = 1/16):
        import sys, tty, termios
        from select import select

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())

            # [ Wait until ready for reading,
            #   wait until ready for writing
            #   wait for an "exception condition" ]
            # The below line times out after 1 second
            # This can be changed to a floating-point value if necessary
            [i, _o, _e] = select([sys.stdin.fileno()], [], [], timeout)
            if i:
                ch = sys.stdin.read(1)
            else:
                ch = None

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch

getch = _Getch()
if __name__ == "__main__":
    getch = _Getch()
    for i in range(1000):
        c = getch()
        if c == 'q':
            break
        else:
            print(c)