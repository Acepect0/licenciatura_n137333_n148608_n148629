from colorama import Fore, Back, Style
from menu.funcoes_visuais import ecra_cheio, Tela, esperar

def ecra_barra_suc():
        # Função que desenha uma barra de carregamento animada ("suc" = sucesso)
    
    
    mensagens = ["A dar corda ás pernas...",
            "A convencer o programador...",
            "A procurar peças em falta...",
            "A soprar o pó dos cartuchos..."]
    with ecra_cheio():
# "with" = enquanto este bloco corre, o ecrã está em modo "cheio".
        # Quando o bloco acaba (ou dá erro), o terminal volta ao normal sozinho.


        p = 0.0
# p = progresso, de 0.0 até 100.0 (percentagem).
        while True:
            t = Tela()
            # tela vazia; t.c = colunas, t.l = linhas do terminal



            # --- Avançar o progresso ---
            presa = p >= 99.9
            if presa:
                p = 100.0     # arredonda para 100 certinho
            else:
                p += max(0.05, (100 - p) * 0.04)
            # anda 4% do que falta (começa rápido, abranda no fim),
            # mas nunca menos de 0.05 para garantir que chega a 100




               # --- Calcular posições ---
            largura = max(10, int(t.c * 0.7))                   # barra = 70% da largura, mínimo 10
            x0, y = (t.c - largura) // 2, t.l // 2              # x0 = coluna inicial (centrada), y = linha do meio
            cheio = int(largura * p / 100)                      # nº de blocos já preenchidos



            # --- Título e mensagem ---
            t.centro(y - 4, "A CARREGAR...", Fore.CYAN + Style.BRIGHT)
            if presa:
                t.centro(y - 2, "Carregamento bem sucedido", Fore.GREEN + Style.BRIGHT)
            else:
                t.centro(y - 2, mensagens[int(p // 12) % len(mensagens)], Fore.YELLOW)
                # muda de frase a cada 12%; o % len(mensagens) faz as frases repetirem em ciclo



             # --- Moldura da barra ---
            t.pôr(x0 - 1, y - 1, "┌" + "─" * largura + "┐", Fore.WHITE)
            t.pôr(x0 - 1, y, "│", Fore.WHITE)
            t.pôr(x0 + largura, y, "│", Fore.WHITE)
            t.pôr(x0 - 1, y + 1, "└" + "─" * largura + "┘", Fore.WHITE)
            # Desenho da moldura da barra de cima, baixo, esquerda e direita


            # --- Interior da barra ---
            t.pôr(x0, y, "█" * cheio, Fore.GREEN)                                               # parte carregada
            t.pôr(x0 + cheio, y, "░" * (largura - cheio), Fore.GREEN + Style.DIM)      # parte por carregar (dim = mais escura)
            
            
            # --- Percentagem e rodapé ---
            t.centro(y + 3, f"{int(p)}%", Fore.WHITE + Style.BRIGHT)
            t.centro(t.l - 2, "Prima uma tecla para voltar", Style.DIM + Fore.WHITE)



            t.mostrar()
            # envia o frame completo para o terminal de uma só vez

            # Tempo de espera entre cada frame
            if esperar(0.03):
                break
