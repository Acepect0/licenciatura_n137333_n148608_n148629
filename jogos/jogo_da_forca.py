import os #Biblioteca "os": permite trabalhar com ficheiros e diretórios do sistema operativo
import unicodedata #Biblioteca "unicodedata": permite trabalhar com caracteres especiais, como acentos e cedilhas
import random #Biblioteca "random": permite gerar números aleatórios, ou escolher aleatoriamente elementos de uma lista
import shutil #Biblioteca "shutil": vamos usar somente para obter a largura da janela do terminal

###  FUNÇÕES  ###
#FUNÇÃO QUE SORTEIA UMA PALAVRA ALEATÓRIA DO FICHEIRO COM AS PALAVRAS
def sortear_palavra(): 
    pasta = os.path.dirname(__file__) #Obtém a localização da pasta onde está este ficheiro Python
    caminho_txt = os.path.join(pasta, 'jogodaforca_palavras.txt') #Junta o diretório gerado pela variável anterior com o nome do ficheiro das palavras
    #Desta forma, o programa vai procurar o ficheiro das palavras na mesma pasta onde o programa está a ser corrido, impedindo erros quando o ficheiro é corrido em computadores diferentes, que podem ter diretórios diferentes
    
    with open(caminho_txt, "r", encoding="utf-8") as palavrastodas: #Abre o ficheiro (localização, modo de leitura, forma de interpretação dos caracteres) E vai fechá-lo assim que a execução do código desta parte terminar
        palavras_com_n = palavrastodas.readlines() #Readlines vai ler o ficheiro todo e devolver uma lista em que cada elemento é uma linha do ficheiro, só que imprime com notações de \n no final de cada elemento

    palavras_limpas = [] #Cria uma lista vazia para depois guardar as palavras limpas, sem /n e espaços
    for linha in palavras_com_n:       #Percorre cada linha da lista gerada pelo readlines
        linha = linha.strip()          #Strip vai remover todos os espaços em branco, tabulações (\t) e quebras de linha (\n)
        if linha != "":                #Se, porventura, existir uma linha vazia, vai ignorá-la, não guardando na lista limpa: Se [palavra] for diferente de um elemento vazio, adiciona à lista limpa
            palavras_limpas.append(linha)     #Guarda na lista limpa

    return random.choice(palavras_limpas)     #Escolhe aleatoriamente uma palavra da lista limpa e devolve-a


#FUNÇÃO QUE REMOVE OS ACENTOS DE UMA LETRA, PARA COMPARAR ENTRE O QUE O JOGADOR ESCREVE E A PALAVRA SORTEADA
def sem_acentos(texto): 
 #Para o computador, por exemplo, "e" e "é" são caracteres diferentes, por isso "e" == "é" dá False. Esta função faz com que o jogador possa escrever "e" e acertar no "é" de "bidé", por exemplo
    resultado = "" 
    for caracter in unicodedata.normalize("NFD", texto): #NFD: Separa os acentos das letras, formando por exemplo "é" = "e´" 
        if unicodedata.category(caracter) != "Mn": #Se o caracter NÃO for um acento solto (Mn), é uma letra (ou hífen), por isso guarda-se. Os acentos soltos são ignorados
            resultado = resultado + caracter
    return resultado


#FUNÇÃO QUE MOSTRA A PALAVRA COM OS ESPAÇOS E LETRAS ACERTADAS
def mostrar_palavra(palavra_sorteada, letras_certas): 
    espacos = ""                                    
    for letra in palavra_sorteada:                  #Percorre cada letra da palavra
        if letra == "-":                            #Se um dos caracteres for um hífen, mostra-o
            espacos = espacos + "- "
        elif sem_acentos(letra) in letras_certas:   #Se uma das letras da palavra estiver na lista de letras_certas, mostra a letra
            espacos = espacos + letra + " "
        else:                                       #Se nenhum dos casos se verificarem, mantém o espaço
            espacos = espacos + "_ "
    return espacos                                  


###  ECRÃ INICIAL ###
if os.name  == "nt": #Se o sistema operativo for Windows, limpa o ecrã com cls
        os.system("cls")            
else:  #Se não for Windows, limpa o ecrã com clear
     os.system("clear")

#Título
largura = shutil.get_terminal_size().columns
largurametade = int(((largura - 17) / 4))
tracos = "⫘⫘" * largurametade
print(f"{tracos}│ JOGO DA FORCA │{tracos}")

print("")
print("Bem-vindo(a) ao Jogo da Forca!")
print("")
print("O objetivo do jogo é acertar a palavra secreta, sabendo apenas o número de letras que ela tem.")
print("Para isso, podes tentar adivinhar uma letra de cada vez, mas só podes errar até 10 vezes.") 
print("Se, a meio da ronda, quiseres arriscar numa só a palavra inteira, podes fazê-lo escrevendo o comando @[o teu palpite]. No entanto, se o teu palpite estiver errado, perdes o jogo.")
print("")
print("Boa sorte!")
print("")

#"Botão de COMEÇAR"
largura = shutil.get_terminal_size().columns
largurametade = int(((largura - 7) / 2))
tracos = " " * largurametade
input(f"{tracos}COMEÇAR{tracos}")


###  PROGRAMA PRINCIPAL  ###

while True: #Mantém o jogo a correr até o jogador decidir sair
    palavra_sorteada = sortear_palavra()

    #VARIÁVEIS DO JOGO
    MAXIMO_DE_ERROS = 10           #Número máximo de erros 
    erros = -1                     #Quantos erros o jogador já cometeu
    letras_certas = []             #Letras que o jogador já acertou
    letras_usadas = []             #Todas as letras já tentadas (certas e erradas)
    mensagem = ""                  #Aviso a mostrar ao jogador 
    venceu = False                 #=True quando o jogador ganha


    #CICLO PRINCIPAL DO JOGO

    while erros < MAXIMO_DE_ERROS and not venceu:   #Repete enquanto o jogador não perdeu nem ganhou
        if os.name  == "nt":
            os.system("cls")            
        else:
            os.system("clear")

        #CABEÇALHO DO JOGO
        largura = shutil.get_terminal_size().columns 
        largurametade = int(((largura - 17)/ 4)) 
        tracos = "⫘⫘" * largurametade
        print(f"{tracos}│ JOGO DA FORCA │{tracos}")

        print("╭———————————————╮")
        print(f"|  Erros: {erros + 1}/{MAXIMO_DE_ERROS}  |")
        print("╰———————————————╯")
        if erros == 10:
            print("╭———————————————╮")
            print(f"| Erros: {erros + 1}/{MAXIMO_DE_ERROS}  |")
            print("╰———————————————╯")
        
        print(f"A palavra tem {len(palavra_sorteada)} letras.")
        print("")
       
        print(mostrar_palavra(palavra_sorteada, letras_certas))
        print(f"Letras usadas: {letras_usadas}")
        print(mensagem)  #Aviso da jogada anterior 
        
        entrada = input("Indica uma letra (ou @ para arriscar): ").lower()

        if entrada.startswith("@"): #Se o jogador iniciar com @
            palpite = entrada.replace("@", "", 1) #Remove o @ do início da palavra

            if palpite == "":
                mensagem = "➤ Escreve o teu palpite depois do @ ou tenta apenas uma letra."

            elif sem_acentos(palpite) == sem_acentos(palavra_sorteada):
                venceu = True

            else:
                erros = MAXIMO_DE_ERROS

        else: #Se o jogador não escrever @, verifica uma letra normal

            tentativa = sem_acentos(entrada)

            # VERIFICAÇÃO DA ENTRADA

            if len(tentativa) != 1 or not tentativa.isalpha(): #isalpha: vê se todos os caractéres são letras do alfabeto, incluindo letras com acento
                mensagem = "➤ Escreve apenas UMA letra. Não escrevas números, símbolos ou palavras."

            elif tentativa in letras_usadas:
                mensagem = "➤ Já tentaste essa letra..."

            else:
                letras_usadas.append(tentativa)

                if tentativa in sem_acentos(palavra_sorteada):
                    letras_certas.append(tentativa)
                    mensagem = "✔ CERTO!"

                    if "_" not in mostrar_palavra(palavra_sorteada, letras_certas):
                        venceu = True

                else:
                    erros = erros + 1
                    mensagem = "✘ Errado..."


###  FIM DO JOGO ###

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    if venceu:
        largura = shutil.get_terminal_size().columns 
        largurametade = int(((largura - 17)/ 4)) 
        tracos = "⫘⫘" * largurametade
        print(f"{tracos}│ JOGO DA FORCA │{tracos}")
        print("")
        largura = shutil.get_terminal_size().columns 
        
        largurametade = int(((largura - 9)/ 2))
        tracos = " " * largurametade

        palavraera = f"Ganhaste! A palavra era [{palavra_sorteada}]"
        largurametade2 = int((largura - len(palavraera)) / 2)
        tracos2 = " " * largurametade2 
       

        desenhovitoria = "꧁⎝ 𓆩༺✧༻𓆪 ⎠꧂"
        largurametade3 = int((largura - len(desenhovitoria)) / 2)
        tracos3 = " " * largurametade3
    
    
        print(f"{tracos3}꧁⎝ 𓆩༺✧༻𓆪 ⎠꧂{tracos3}")

        
        print(f"{tracos} PARABÉNS{tracos}") 
        print(f"{tracos2}{palavraera}{tracos2}")
        
        
    else:
        largura = shutil.get_terminal_size().columns 
        largurametade = int((largura - 17) / 4) 
        tracos = "⫘⫘" * largurametade
        print(f"{tracos}│ JOGO DA FORCA │{tracos}")
        print("")

        largurametade4 = int((largura - 8) / 2) 
        tracos4 = " " * largurametade4
        largurametade5 = int((largura - 11) / 2)
        tracos5 = " " * largurametade5
    
        palavraera1 = f"A palavra era [{palavra_sorteada}]"
    
        largurametade6 = int((largura - len(palavraera1)) / 2)
        tracos6 = " " * largurametade6
    
        print(f"{tracos4}(·•᷄_•᷅ ){tracos4}")
        print(f"{tracos5}Perdeste...{tracos5}")
        print(f"{tracos6}{palavraera1}{tracos6}")


    print("")
    continuar = input("Para jogar novamente, prime Enter ou escreve «Sair» para saíres do jogo: ").lower()

    if continuar == "sair":
        break