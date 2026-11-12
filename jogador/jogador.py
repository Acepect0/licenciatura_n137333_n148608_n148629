from colorama import Fore, Style, Back 
import shutil

#FUNÇÃO QUE MOSTRA UM TÍTULO ENCOSTADO À ESQUERDA, COM A DECORAÇÃO A PREENCHER O RESTO DA LINHA
def titulo_esquerdo(cor, titulo, decoracao): 
    largura = shutil.get_terminal_size().columns
    repeticoes = (largura - len(titulo) - len(decoracao) * 2) // len(decoracao) 
    lados = decoracao * repeticoes 

    print(cor + f"{decoracao * 2}{titulo}{lados}") 

def jogadores():
    # A mensagem correspondente à escolha do utilizador
    titulo_esquerdo(Fore.LIGHTCYAN_EX, "| UTILIZADORES |","——")

    print(Fore.GREEN + "1 - Escolha um utlizador existente")
    print(Fore.RED + "2 - Crie um novo utilizador.")
    
    escolha = int(input(""))

jogadores()