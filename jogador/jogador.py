from colorama import Fore, Style, Back 
import shutil
largura = shutil.get_terminal_size().columns #Importa a largura, o número de colunas do terminal
largurametade = int((largura - 16)- 2) #Subtrai a largura completa por 16, o número de caracteres de "│ UTILIZADORES │" e subtrai ainda por 2, número de caracteres de "——"
tracos = "—" * largurametade #Cria a string de traços

def jogadores():
    # A mensagem correspondente à escolha do utilizador
    print(Fore.LIGHTCYAN_EX + f"{"——"}│ UTILIZADORES │{tracos}")

    print(Fore.GREEN + "1 - Escolha um utlizador existente")
    print(Fore.RED + "2 - Crie um novo utilizador.")
    
    escolha = int(input(""))

jogadores()