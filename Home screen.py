"""
Menu Principal do Projeto Final 

@description: menu inicial do projeto final da unidade curricular de Fundamentos de programação
@version: 0.0.1v
@author: Alexandre Rogado, nº137333 - Martim Soares, nº148608 - Rúben Gaspar, nº148629
"""

from colorama import Fore, Back, Style, init
from jogos import main
from .funcoes_visuais import ecra_cheio, esperar, Tela
from menu.manutencao import em_manutencao
from menu.barra_transicao_bem_sucedida import ecra_barra_suc
from menu.barra_transicao_mal_sucedida import ecra_barra_mal

init(autoreset=True)

def menu():
    # A mensagem correspondente á escolha do utilizador
    print("----- Utilizadores -----")
    print("1 - Escolha um utilizador existente")
    print("2 - Crie um novo utilizador.")

    escolha = int(input("Introduza a sua opção: "))

    if escolha == 1:
        ecra_barra_mal()
        em_manutencao()
    else:
        ecra_barra_mal()
        em_manutencao()

    print(" ----- Menu -----")
    print(" 1 - Historico ")
    print(" 2 - Rankings ")
    print(" 3 - Jogos ")
    print(" 4 - Gerir Perfil")
    print(" 5 - Mudar de Jogador ")
    print(" 6 - Sair ")

    opcao = int(input("Selecione a opção do Menu que pretende: "))

    match opcao:
        case 1:
            ecra_barra_suc()
        case 2:
            ecra_barra_mal()
        case 3:
            ecra_barra_suc()
        case 4:
            ecra_barra_mal()
            em_manutencao()
        case 5:
            ecra_barra_mal()
            em_manutencao()
        case 6:
            print("Até á próximo!")

    main.jogos()

menu()