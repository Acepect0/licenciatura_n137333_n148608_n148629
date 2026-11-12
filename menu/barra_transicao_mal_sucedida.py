from funcoes_visuais import Tela, ecra_cheio, esperar
from colorama import Fore, Back, Style

# ======================================================================
#  Barra de progresso gigante que encrava nos 87%
# ======================================================================
def ecra_barra_mal():
    msgs = ["A aquecer os motores...",
            "A convencer o programador...",
            "A procurar peças em falta...",
            "A soprar o pó dos cartuchos..."]
    with ecra_cheio():
        p = 0.0
        while True:
            t = Tela()
            presa = p >= 86.9
            if presa:
                p = 87.0
            else:
                p += max(0.05, (87 - p) * 0.04)

            largura = max(10, int(t.c * 0.7))
            x0, y = (t.c - largura) // 2, t.l // 2
            cheio = int(largura * p / 100)

            t.centro(y - 4, "A CARREGAR...", Fore.CYAN + Style.BRIGHT)
            if presa:
                t.centro(y - 2, "ERRO! Falha no carregamento! ", Fore.RED + Style.BRIGHT)
            else:
                t.centro(y - 2, msgs[int(p // 12) % len(msgs)], Fore.YELLOW)

            t.pôr(x0 - 1, y - 1, "┌" + "─" * largura + "┐", Fore.WHITE)
            t.pôr(x0 - 1, y, "│", Fore.WHITE)
            t.pôr(x0 + largura, y, "│", Fore.WHITE)
            t.pôr(x0 - 1, y + 1, "└" + "─" * largura + "┘", Fore.WHITE)
            t.pôr(x0, y, "█" * cheio, Fore.GREEN)
            t.pôr(x0 + cheio, y, "░" * (largura - cheio), Fore.GREEN + Style.DIM)
            t.centro(y + 3, f"{int(p)}%", Fore.WHITE + Style.BRIGHT)
            t.centro(t.l - 2, "Prima uma tecla para voltar", Style.DIM + Fore.WHITE)
            t.mostrar()
            if esperar(0.03):
                break
ecra_barra_mal()