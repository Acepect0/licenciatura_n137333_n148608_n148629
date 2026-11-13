import os       # Permite obter informações sobre o sistema operativo
import sys      # Dá acesso ao teclado

# Transforma uma função no bloco para ser usada como with
from contextlib import contextmanager    

# Usado apenas para levar Reset
from colorama import Style

# Decorador que permite mudar o comportamento de uma função
@contextmanager
def ecra_cheio():
    """Entra no 'ecrã alternativo' do terminal, esconde o cursor e
    repõe tudo no fim (mesmo que haja um erro ou Ctrl+C)."""

    # fileDescriptor identifica o teclado que vai ser usado
    # defOriginais é as definições originais do teclado 
    # Estão colocadas como None porque o windows não os usa
    fileDescriptor = defOriginais = None

    # Como o Windows é cotado como "nt", tudo o que NÃO estiver no Windows vai executar o bloco
    if os.name != "nt":

        # Imports para controlar o comportamento do terminal (fora do topo, para não dar erro no Windows)
        import termios
        import tty

        # Número que identifica o teclado 
        fileDescriptor = sys.stdin.fileno()

        # Tira uma "print" ás definições atuais do teclado, para repo-las no fim
        defOriginais = termios.tcgetattr(fileDescriptor)

        # Ativa o modo cbreak, isto é, as teclas escritas não aparecem no ecrã, mantendo assim a animação límpa
        tty.setcbreak(fileDescriptor)
    
    # Códigos que o terminal percebe como comandos em vez de texto
    # \033 é o inicio do comando 
    # 
    # \033[?1049h - Comando que muda para o ecrã alternativo
    # \033[?251 - Comando que esconde o cursor 
    # \033[2J - Comando que limpa o terminal completamente
    sys.stdout.write("\033[?1049h\033[?25l\033[2J")

    # A função flush() obriga os comandos a serem mandados obrigatóriamente
    sys.stdout.flush()

    # O yield *pausa* a função do ecra_cheio() e executa a animação atribuída.
    # Quando a animação termina a função continua a onde estava
    try:
        yield

    # Este finally permite a limpeza e reposição das definições originais
    finally:

        #Style.RESET_ALL: repõe as cores ao normal.
        # \033[?25h: mostra o cursor outra vez.
        # \033[?1049l: sai do ecrã alternativo e volta ao ecrã anterior.
        sys.stdout.write(Style.RESET_ALL + "\033[?25h\033[?1049l")

        # Novamente, obriga a execução imediata dos comandos
        sys.stdout.flush()

        # Irá apenas executar caso o sistema operativo seja diferente de Windows
        if fileDescriptor is not None:

            # Repõe as definições iniciais ("fotografadas" anteriormente)
            # \type: ignore serve apenas para não aparecer a mensagem de warning do editor
            termios.tcsetattr(fd, termios.TCSADRAIN, defOriginais) # type: ignore

            # Qualquer tecla pressionada durante a animação será aqui descartada
            termios.tcflush(fd, termios.TCIFLUSH) # type: ignore