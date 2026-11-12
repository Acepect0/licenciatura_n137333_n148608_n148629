from colorama import Fore, Style, Back
from jogos.match_case import match_case
import shutil

largura = shutil.get_terminal_size().columns
largurametade = int((largura - 14) / 2)
tracos = "-" * largurametade

def jogos():
    print(Fore.YELLOW + tracos + " JOGOS " + tracos)
    print(Fore.LIGHTBLUE_EX + "1 - Adivinha o número")
    print(Fore.GREEN + "2 - Pedra, Papel ou Tesoura")
    print(Fore.MAGENTA + "3 - Jogo da Forca")
    print(Fore.RED + "0 - Sair")

    opcao = int(input(Fore.RESET + "Introduza a sua opção: "))

    match_case(opcao)
