#coisas a ter em conta:
# - o programa tem de randomizar palavras atoa, e tem de ser palavras reais, não palavras inventadas
# - interface visual

import random
import os #A biblioteca "os" permite trabalhar com ficheiros e diretórios do sistema operativo

def sortear_palavra():
    pasta = os.path.dirname(__file__) #Obtém a localização da pasta onde está este ficheiro Python
    caminho_txt = os.path.join(pasta, 'jogodaforca_palavras.txt') #Junta o diretório gerado pela variável anterior com o nome do ficheiro das palavras
    
    with open(caminho_txt, "r", encoding="utf-8") as ficheiro: #Abre o ficheiro (localização, modo de leitura, forma de interpretação dos caracteres)
        palavras_com_n = ficheiro.readlines() #Readlines vai ler o ficheiro todo e devolver uma lista em que cada elemento é uma linha do ficheiro, só que imprime com notações de \n no final de cada elemento

    palavras = [] #Cria uma lista vazia para depois guardar as palavras limpas, sem /n e espaços
    for linha in palavras_com_n:       #Percorre cada linha da lista gerada pelo readlines
        linha = linha.strip()          #Strip vai remover todos os espaços em branco, tabulações (\t) e quebras de linha (\n)
        if linha != "":                #Se, porventura, existir uma linha vazia, vai ignorá-la, não guardando na lista limpa: Se [palavra] for diferente de um elemento vazio, adiciona à lista limpa
            palavras.append(linha)     #Guarda na lista limpa

    return random.choice(palavras)     #Escolhe aleatoriamente uma palavra da lista limpa e devolve-a

palavra_sorteada = sortear_palavra()
# print(palavra_sorteada)

#titulo e coisas giras

print("")
#Colocar aqui um timer algures para nao ser tudo tao rapido, tp "a gerar palavra..."
print("Palavra sorteada. A palavra tem", len(palavra_sorteada), "letras. Boa sorte!")

def mostrar_palavra(palavra, letras_certas):
    espacos = ""                               #Texto que vamos construindo
    for letra in palavra:                      #Percorre cada letra da palavra
        if letra == "-":                       #Hífen aparece sempre
            espacos = espacos + "- "
        elif letra in letras_certas:           #Letra já acertada: mostra-a
            espacos = espacos + letra + " "
        else:                                  #Letra por descobrir: mostra _
            espacos = espacos + "_ "
    return espacos                             #Devolve o texto pronto


# ---------- Programa principal ----------

palavra_sorteada = sortear_palavra()
# print(palavra_sorteada)   # descomenta para testar

#titulo e coisas giras

print("")
#Colocar aqui um timer algures para nao ser tudo tao rapido, tp "a gerar palavra..."
print("Palavra sorteada. A palavra tem", len(palavra_sorteada), "letras. Boa sorte!")

letras_certas = []                             #Letras que o jogador já acertou

while True:                                    #Repete até pararmos (Ctrl+C)
    print(mostrar_palavra(palavra_sorteada, letras_certas))
    tentativa = input("Escolhe uma letra: ").lower()   #Pede letra, em minúsculas

    if tentativa in palavra_sorteada:          #Está na palavra?
        letras_certas.append(tentativa)        #Guarda como certa
        print("Certa!")
    else:
        print("Errada!")

#fazer uma feature de adivinhar uma palavra inteira, e se acertar, ganha o jogo, se errar, perde. so tem uma tentativa