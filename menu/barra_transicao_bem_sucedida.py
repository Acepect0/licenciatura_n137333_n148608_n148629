from colorama import Fore, Back, Style
from menu.funcoes_visuais import ecra_cheio, Tela, esperar
import time

def ecra_barra_suc():

    # Mensagens que irão aparecer ao longo do carregamento da barra de progresso
    mensagens = [
        "A carregar o conteúdo...",
        "A convencer o programador...",
        "A procurar peças em falta...",
    ]

    # Entra no modo de ecrã cheio (respetiva documentação no ficheiro da função)
    with ecra_cheio():

        # Percentagem inicial da barra de progresso
        percentagem = 0.0

        # Instante em que a barra de progresso chega a 100 %
        inicio_fim = None

        while True:
            tela = Tela()

            # Percentagem final da barra de progresso
            fim = percentagem >= 99.9

            # Se a barra chegar ao fim, a percentagem é máxima 
            # Até lá, irá aumentar mais rapidamente no inicio e mais lentamente no fim
            if fim:
                percentagem = 100.0

                # Garante que o relógio não reinicia a cada frame de progresso
                if inicio_fim is None:
                    inicio_fim = time.monotonic()
            else:
                percentagem += max(0.05, (100 - percentagem) * 0.04)

            # A barra ocupa 70 % das colunas do terminal, com um mínimo 10
            largura = max(10, int(tela.c * 0.7))

            # x0 = local onde a barra começa 
            # y = linha central do terminal
            x0, y = (tela.c - largura) // 2, tela.l // 2

            # Número de blocos a preencher, sendo proporcional á percentagem
            cheio = int(largura * percentagem / 100)

            # Textos que aparecem por cima da barra de Progresso
            tela.centro(y - 4, "A CARREGAR...", Fore.CYAN + Style.BRIGHT)
            if fim:
                tela.centro(y - 2, "Carregamento bem sucedido", Fore.GREEN + Style.BRIGHT)
            else:

                # Muda as mensagens a cada 12 % da barra 
                tela.centro(y - 2, mensagens[int(percentagem // 12) % len(mensagens)], Fore.YELLOW)

            # Desenha a moldura da barra de progresso
            tela.pôr(x0 - 1, y - 1, "┌" + "─" * largura + "┐", Fore.WHITE)
            tela.pôr(x0 - 1, y, "│", Fore.WHITE)
            tela.pôr(x0 + largura, y, "│", Fore.WHITE)
            tela.pôr(x0 - 1, y + 1, "└" + "─" * largura + "┘", Fore.WHITE)

            # Parte preenchida da barra e parte por preencher da barra
            tela.pôr(x0, y, "█" * cheio, Fore.GREEN)
            tela.pôr(x0 + cheio, y, "░" * (largura - cheio), Fore.GREEN + Style.DIM)

            # Mostra a percentagem atual da barra
            tela.centro(y + 3, f"{int(percentagem)}%", Fore.WHITE + Style.BRIGHT)

            # Mostra cada frame da barra
            tela.mostrar()

            # Pausa entre fotogramas (a tecla premida, se houver, é ignorada)
            esperar(0.03)

            # Passados 2 segundos depois da barra ter terminado de carregar, sai automaticamente
            if inicio_fim is not None and time.monotonic() - inicio_fim >= 2:
                break