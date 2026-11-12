from colorama import Fore, Back, Style
from menu.funcoes_visuais import ecra_cheio, esperar, Tela

def em_manutencao():
    """Ecrã mostrado quando uma funcionalidade ainda não está pronta."""
    with ecra_cheio():
        off = 0
        while True:
            t = Tela()
            for y in range(t.l):
                for x in range(t.c):
                    if x < 4 or x >= t.c - 4 or y < 2 or y >= t.l - 2:
                        cor = Back.YELLOW if ((x + 2 * y + off) // 4) % 2 == 0 else Back.BLACK
                        t.g[y][x] = (" ", cor)

            m = t.l // 2
            amarelo = Fore.YELLOW + Style.BRIGHT
            t.centro(m - 3, "/!\\  OBRAS EM CURSO  /!\\", amarelo)
            t.centro(m - 1, "Esta secção ainda não está pronta.", Fore.WHITE)
            t.centro(m, "Volte em breve.", Fore.WHITE)
            t.centro(m + 3, "Prima uma tecla para voltar", Style.DIM + Fore.WHITE)
            t.mostrar()
            off += 1
            if esperar(0.12):
                break