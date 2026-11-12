from colorama import Fore, Style, Back 
import shutil
largura = shutil.get_terminal_size().columns #Importa a largura, o número de colunas do terminal
largurametade = int((largura - 16)- 2) #Subtrai a largura completa por 16, o número de caracteres de "│ UTILIZADORES │" e subtrai ainda por 2, número de caracteres de "——"
tracos = "—" * largurametade #Cria a string de traços

def perfil():
    # A mensagem correspondente à escolha do utilizador
    print(Fore.LIGHTCYAN_EX + f"{"——"}│ GERIR PERFIL │{tracos}")

perfil()