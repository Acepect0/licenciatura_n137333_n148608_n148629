from colorama import Fore, Style, Back 
import shutil
largura = shutil.get_terminal_size().columns
largurametade = int((largura - 14) / 2)
tracos = "-" * largurametade

def jogadores():
    # A mensagem correspondente á escolha do utilizador
    print(Fore.LIGHTCYAN_EX + f"{tracos} UTILIZADORES {tracos}")

    print(Fore.GREEN + "1 - Escolha um utlizador existente")
    print(Fore.RED + "2 - Crie um novo utilizador.")
    
    escolha = int(input(""))

jogadores()