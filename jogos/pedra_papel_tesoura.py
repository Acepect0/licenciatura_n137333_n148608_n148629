# Pedra, Papel ou Tesoura
# Regra de fim de partida: ganha quem chegar primeiro a 3 vitórias.

import random  # necessário para o computador escolher ao acaso
from colorama import Fore, Style, Back



VITORIAS_PARA_GANHAR = 3   # constante (nome em maiúsculas)
PONTOS_POR_VITORIA = 10
PONTOS_POR_EMPATE = 3

print(Fore.RED + "===== PEDRA, PAPEL OU TESOURA =====")
print(Fore.WHITE + f"Objetivo: ser o primeiro a chegar a {VITORIAS_PARA_GANHAR} vitórias.")
print(Fore.WHITE + "Regras: Pedra vence Tesoura | Tesoura vence Papel | Papel vence Pedra")
print(Fore.WHITE + "Opções: 1 - Pedra | 2 - Papel | 3 - Tesoura | 0 - Desistir")


#Contadores da partida
vitorias_jogador = 0
vitorias_computador = 0
empates = 0
ronda = 0


# Loop principal do jogo, continua até que um dos jogadores atinja o número de vitórias necessárias para ganhar
while vitorias_jogador < VITORIAS_PARA_GANHAR and vitorias_computador < VITORIAS_PARA_GANHAR:
    ronda = ronda + 1
    print(Fore.YELLOW + f"\nRonda {ronda}---")
    print(Fore.YELLOW + f"Vitórias do jogador: {vitorias_jogador} | Vitórias do computador: {vitorias_computador} | Empates: {empates}")

# Solicitar a escolha do jogador
    try:
        escolha_jogador = int(input("A sua escolha (1/2/3, 0 para desistir): "))
    except ValueError:
        print("Erro: tem de introduzir um número.")
        continue  # volta ao início do ciclo sem contar a ronda

    if escolha_jogador == 0:
        print("Desistiu da partida.")
        break
    elif escolha_jogador < 1 or escolha_jogador > 3:
        print("Opção inválida. Escolha 1, 2 ou 3.")
        continue

        # ---- Escolha do computador ----
    escolha_computador = random.randint(1, 3)

    # ---- Converter numeros em nomes para mostrar ao utilizador ----
    if escolha_jogador == 1:
        nome_jogador = "Pedra"
    elif escolha_jogador == 2:
        nome_jogador = "Papel"
    else:
        nome_jogador = "Tesoura"

    if escolha_computador == 1:
        nome_computador = "Pedra"
    elif escolha_computador == 2:
        nome_computador = "Papel"
    else:
        nome_computador = "Tesoura"

    print(f"Você: {nome_jogador}  |  Computador: {nome_computador}")