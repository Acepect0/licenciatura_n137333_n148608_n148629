import os
import sys
from contextlib import contextmanager
from colorama import Style

@contextmanager
def ecra_cheio():
    """Entra no 'ecrã alternativo' do terminal, esconde o cursor e
    repõe tudo no fim (mesmo que haja um erro ou Ctrl+C)."""
    fd = antigo = None
    if os.name != "nt":
        import termios
        import tty
        fd = sys.stdin.fileno()
        antigo = termios.tcgetattr(fd)
        tty.setcbreak(fd)
    sys.stdout.write("\033[?1049h\033[?25l\033[2J")
    sys.stdout.flush()
    try:
        yield
    finally:
        sys.stdout.write(Style.RESET_ALL + "\033[?25h\033[?1049l")
        sys.stdout.flush()
        if fd is not None:
            termios.tcsetattr(fd, termios.TCSADRAIN, antigo)
            termios.tcflush(fd, termios.TCIFLUSH)

