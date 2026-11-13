"""
Menu Principal do Projeto Final

@description: menu inicial do projeto final da unidade curricular de Fundamentos de programação
@version: 0.0.1v
@author: Alexandre Rogado, nº137333 - Martim Soares, nº148608 - Rúben Gaspar, nº148629
"""

from colorama import Fore, Back, Style, init
from jogos import main
from menu.funcoes_visuais import ecra_cheio, esperar, Tela
from menu.manutencao import em_manutencao
from menu.barra_transicao_bem_sucedida import ecra_barra_suc
from menu.barra_transicao_mal_sucedida import ecra_barra_mal

init(autoreset=True)


def utilizador():
    # A mensagem correspondente á escolha do utilizador
    print("----- Utilizadores -----")
    print(
        "1 - Escolha um utilizador existente          " + Fore.YELLOW + "EM MANUTENÇÃO"
    )
    print("2 - Crie um novo utilizador.")

    escolha = int(input("Introduza a sua opção: "))

    if escolha == 1:  # ligar a jogador/mudar_jogador.py quando estiver pronto
        ecra_barra_mal()
        em_manutencao()

    else:  # ligar a jogador/criar_jogador.py quando estiver pronto
        ecra_barra_mal()
        em_manutencao()


def menu():
    """Menu principal. Fica em ciclo até o utilizador escolher Sair."""

    statusUtilizador = False
    while True:

        if statusUtilizador == False:
            utilizador()
            statusUtilizador = True

        print(" ----- ARCADE -----")
        print(" 1 - Historico ")
        print(" 2 - Rankings ")
        print(" 3 - Jogos ")
        print(" 4 - Gerir Perfil")
        print(" 5 - Mudar de Jogador ")
        print(" 6 - Sair ")

        opcao = int(input("Selecione a opção do Menu que pretende: "))

        if opcao == 1:
            ecra_barra_mal()
            em_manutencao()
        elif opcao == 2:
            ecra_barra_mal()
            em_manutencao()
        elif opcao == 3:
            ecra_barra_suc()
            main.jogos()  # só entra nos jogos quando o utilizador escolhe 3
        elif opcao == 4:
            ecra_barra_mal()
            em_manutencao()
        elif opcao == 5:
            ecra_barra_mal()
            em_manutencao()
            # ecra_utilizadores()   # mudar de jogador volta ao ecrã de utilizadores Criar menu de utilizadores
        else:
            print(f"Até à próxima!")
            break  # sai do ciclo e termina o programa


if __name__ == "__main__":
    menu()
