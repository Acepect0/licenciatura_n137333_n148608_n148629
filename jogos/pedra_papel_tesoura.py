# Pedra, Papel ou Tesoura
# Regra de fim de partida: ganha quem chegar primeiro a 3 vitórias.

import random  # necessário para o computador escolher ao acaso
from colorama import Fore, Back, Style, init


VITORIAS_PARA_GANHAR = 3   # constante (nome em maiúsculas)
PONTOS_POR_VITORIA = 10
PONTOS_POR_EMPATE = 3

init(autoreset=True)  # Inicializar o colorama

print(f"{Fore.CYAN}===== PEDRA, PAPEL OU TESOURA =====")
print(f"{Fore.WHITE}Objetivo: ser o primeiro a chegar a {VITORIAS_PARA_GANHAR} vitórias.")
print(f"{Fore.WHITE}Regras: Pedra vence Tesoura | Tesoura vence Papel | Papel vence Pedra")
print(f"{Fore.WHITE}Opções: Pedra | Papel | Tesoura | Desistir")

#Contadores da partida
vitorias_jogador = 0
vitorias_computador = 0
empates = 0
ronda = 0

jogar_novamente = True
partida = 0


# ===== Ciclo exterior: uma volta por partida =====
while jogar_novamente:
    partida = partida + 1
    print(f"\n########## PARTIDA {partida} ##########")

    # Reiniciar contadores a cada partida
    vitorias_jogador = 0
    vitorias_computador = 0
    empates = 0
    ronda = 0

    # Loop principal do jogo, continua até que um dos jogadores atinja o número de vitórias necessárias para ganhar
    while vitorias_jogador < VITORIAS_PARA_GANHAR and vitorias_computador < VITORIAS_PARA_GANHAR:
        ronda = ronda + 1
        print(f"\nRonda {ronda}---")
        print(f"Vitórias do jogador: {vitorias_jogador} | Vitórias do computador: {vitorias_computador} | Empates: {empates}")

    # Solicitar a escolha do jogador
        escolha_jogador = input("A sua escolha (pedra/papel/tesoura, sair para desistir): ").strip().lower()

        #O srip() remove espaços em branco no início e no fim da string, e lower() converte a string para minúsculas.

        if escolha_jogador == "sair":
            print("Desistiu da partida.")
            break
        elif escolha_jogador != "pedra" and escolha_jogador != "papel" and escolha_jogador != "tesoura":
            print("Opção inválida. Escreva pedra, papel ou tesoura.")
            ronda = ronda - 1
            continue
        

    # ---- Escolha do computador ----
        escolha_computador = random.choice(["pedra", "papel", "tesoura"])

        print(escolha_computador)  # Imprime uma palavra aleatória da lista


        print(f"Você: {escolha_jogador}  |  Computador: {escolha_computador}")


        #---- Determinar o vencedor da ronda ----
        if escolha_jogador == escolha_computador:
            print("Empate!")
            empates += 1
        elif(escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
            (escolha_jogador == "tesoura" and escolha_computador == "papel") or \
            (escolha_jogador == "papel" and escolha_computador == "pedra"):
            print("Ganhou a ronda!")
            vitorias_jogador = vitorias_jogador + 1
        else:
            print("Perdeste. O computador venceu a ronda!")
            vitorias_computador += 1


    #---- Mostrar o resultado final da partida ----
    print("\n===== FIM DA PARTIDA =====")
    print(f"Rondas jogadas: {ronda}")

    # Pontuações (mesma fórmula para os dois)
    pontuacao_jogador = vitorias_jogador * PONTOS_POR_VITORIA + empates * PONTOS_POR_EMPATE
    pontuacao_computador = vitorias_computador * PONTOS_POR_VITORIA + empates * PONTOS_POR_EMPATE


    if vitorias_jogador == VITORIAS_PARA_GANHAR:
            print("\n--- Os seus resultados ---")
            print(f"Vitórias:   {vitorias_jogador}")
            print(f"Derrotas:   {vitorias_computador}")
            print(f"Empates:    {empates}")
            print(f"Pontuação:  {pontuacao_jogador}")

            print("\n--- Resultados do computador ---")
            print(f"Vitórias:   {vitorias_computador}")
            print(f"Derrotas:   {vitorias_jogador}")
            print(f"Empates:    {empates}")
            print(f"Pontuação:  {pontuacao_computador}")

            print()
            if vitorias_jogador == VITORIAS_PARA_GANHAR:
                print("Parabéns, venceu a partida!")
            elif vitorias_computador == VITORIAS_PARA_GANHAR:
                print("O computador venceu a partida.")
            else:
                print("Partida terminada sem vencedor.")



# ---- Perguntar se quer jogar outra vez (com validação) ----
    resposta = ""
    while resposta != "s" and resposta != "n":
        resposta = input("\nJogar outra partida? (s/n): ").lower()
        if resposta != "s" and resposta != "n":
            print("Responda apenas com s ou n.")

    if resposta == "n":
        jogar_novamente = False

print("\nObrigado por jogar!")