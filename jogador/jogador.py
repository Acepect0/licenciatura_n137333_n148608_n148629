from colorama import Fore, Style, Back

def jogadores():
    # A mensagem correspondente á escolha do utilizador
    print(Fore.LIGHTCYAN_EX + "------------------ UTILIZADORES ------------------")

    print(Fore.GREEN + "1 - Escolha um utlizador existente")
    print(Fore.RED + "2 - Crie um novo utilizador.")
    
    escolha = int(input(""))

jogadores()