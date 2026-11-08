from colorama import Fore, Style, Back 
import shutil
largura = shutil.get_terminal_size().columns #Importa a largura, o número de colunas do terminal
largurametade = int((largura - 14) / 2) #Calcula o número de traços de cada lado, subtraindo 14, que é o tamanho da string " UTILIZADORES " e dividindo por 2
tracos = "-" * largurametade #Cria a string de traços

def jogadores():
    # A mensagem correspondente á escolha do utilizador
    print(Fore.LIGHTCYAN_EX + f"{tracos} UTILIZADORES {tracos}")

    print(Fore.GREEN + "1 - Escolha um utlizador existente")
    print(Fore.RED + "2 - Crie um novo utilizador.")
    
    escolha = int(input(""))

jogadores()