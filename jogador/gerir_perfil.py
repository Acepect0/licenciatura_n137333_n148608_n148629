from colorama import Fore, Style, Back 
import shutil

#FUNÇÃO QUE MOSTRA UM TÍTULO ENCOSTADO À ESQUERDA, COM A DECORAÇÃO A PREENCHER O RESTO DA LINHA
def titulo_esquerdo(cor, titulo, decoracao): 
    largura = shutil.get_terminal_size().columns
    repeticoes = (largura - len(titulo) - len(decoracao) * 2) // len(decoracao) 
    lados = decoracao * repeticoes 

    print(cor + f"{decoracao * 2}{titulo}{lados}") 

def perfil():
    titulo_esquerdo(Fore.LIGHTCYAN_EX, "│ GERIR PERFIL │", "——")
    

perfil()