from menu.funcoes_visuais import Tela, ecra_cheio, esperar
from colorama import Fore, Back, Style
import time

def ecra_barra_mal():

    # As mensagens que iram aparecer por cima da barra de carregamento
    mensagens = ["A carregar o conteúdo...", 
            "A convencer o programador...",
            "A procurar peças em falta...",]

    # Entra em modo de ecrâ inteiro, de acordo com a documentação escrita no próprio documento
    with ecra_cheio():

        # Percentagem Inicial da Barra
        percentagem = 0.0

        # Instante assim que apresenta a mensagem de erro de carregamento
        inicio_erro = None

        #Loop da Barra (em que cada ciclo é um frame)
        while True:

            # Ecrã Limpa para cada fotograma
            t = Tela()

            # Ponto em que a barra irá ficar "presa"
            presa = percentagem >= 86.9

            # Se percentagem atingir o limite, a barra fica presa
            # Até lá, a percentagem vai aumentando rápido quando está longe e mais devagar ao aproximar-se
            if presa:
                percentagem = 87.0

                # Guarda o momento do erro apenas na primeira vez
                if inicio_erro is None:
                    inicio_erro = time.monotonic()
            else:
                percentagem += max(0.05, (87 - percentagem) * 0.04)

            # A barra ocupa 70% da largura do terminal, sendo no minimo 10
            largura = max(10, int(t.c * 0.7))

            # x0 = Coluna em que a barra começa
            # y = Coluna que se encontra ao meio do ecrã
            x0, y = (t.c - largura) // 2, t.l // 2

            # Número de carácteres preenchidos, sendo proporcional com a percentagem
            cheio = int(largura * percentagem / 100)

            # Título centrado, estando 4 linhas acima do meio
            t.centro(y - 4, "A CARREGAR...", Fore.CYAN + Style.BRIGHT)

            # Quando chega ao 87 %, mostra a mensagem a vermelho da falha de carregamento
            # Em cada 12 %, a mensagem muda, iterando assim pela
            # % len(mensagens) ajuda a não iterar fora dos indices da lista, voltando ao inicio quando passa da última
            if presa:
                t.centro(y - 2, "ERRO! Falha no carregamento! ", Fore.RED + Style.BRIGHT)
            else:
                t.centro(y - 2, mensagens[int(percentagem // 12) % len(mensagens)], Fore.YELLOW)

            # Desenho da moldura da barra de cima, baixo, esquerda e direita
            t.pôr(x0 - 1, y - 1, "┌" + "─" * largura + "┐", Fore.WHITE)
            t.pôr(x0 - 1, y, "│", Fore.WHITE)
            t.pôr(x0 + largura, y, "│", Fore.WHITE)
            t.pôr(x0 - 1, y + 1, "└" + "─" * largura + "┘", Fore.WHITE)

            # Parte preenchida ao longo do tempo na barra
            t.pôr(x0, y, "█" * cheio, Fore.GREEN)

            # Parte por preencher ao longo do tempo
            t.pôr(x0 + cheio, y, "░" * (largura - cheio), Fore.GREEN + Style.DIM)

            # Mostra a percentagem por baixo da mensagem
            t.centro(y + 3, f"{int(percentagem)}%", Fore.WHITE + Style.BRIGHT)

            # Imprime a tela no terminal
            t.mostrar()
            
            # Tempo de espera entre cada frame
            esperar(0.03)

            # Assim que aparece a mensagem de erro, passados 2 segundos avança para outra fase
            if inicio_erro is not None and time.monotonic() - inicio_erro >= 2:
                break