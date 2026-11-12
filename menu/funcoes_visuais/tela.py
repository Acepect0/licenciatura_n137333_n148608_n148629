import shutil
import sys
from colorama import Style

class Tela:
    """Uma grelha de (carácter, estilo) com o tamanho atual do terminal.
    Desenha-se tudo de uma vez por frame, o que evita cintilação."""

    def __init__(self, base=""):
        self.c, self.l = shutil.get_terminal_size()
        self.base = base
        self.g = [[(" ", base)] * self.c for _ in range(self.l)]

    def pôr(self, x, y, txt, estilo=""):
        if not 0 <= y < self.l:
            return
        for i, ch in enumerate(txt):
            if 0 <= x + i < self.c:
                self.g[y][x + i] = (ch, self.base + estilo)

    def centro(self, y, txt, estilo=""):
        self.pôr((self.c - len(txt)) // 2, y, txt, estilo)

    def mostrar(self):
        linhas = []
        for linha in self.g:
            s, atual = "", None
            for ch, est in linha:
                if est != atual:
                    s += Style.RESET_ALL + est
                    atual = est
                s += ch
            linhas.append(s + Style.RESET_ALL)
        sys.stdout.write("\033[H" + "\n".join(linhas))
        sys.stdout.flush()