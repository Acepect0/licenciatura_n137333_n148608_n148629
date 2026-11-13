from colorama import Fore, Style, Back 
import shutil


# Lista onde ficam guardados os jogadores criados (por agora só em memória)
# Está fora das funções para que todas possam ler e escrever nela.
# Por agora só existe em memória: ao fechar o programa, desaparece.
jogadores_registados = []


def escolher_jogador():
    """Mostra os jogadores existentes e devolve o nome escolhido (ou None se não houver)."""
    titulo_esquerdo(Fore.LIGHTCYAN_EX, "| ESCOLHER UTILIZADOR |", "—")              # cabeçalho do ecrã



     # Se a lista está vazia, avisa e devolve None (sinal de "não há jogador escolhido")
    if len(jogadores_registados) == 0:
        print(Fore.YELLOW + "Não existem jogadores criados.")
        return None

     # Mostra os jogadores numerados a partir de 1 (as listas começam em 0, por isso i + 1)
    for i in range(len(jogadores_registados)):
        print(f"{i + 1} - {jogadores_registados[i]}")

    escolha = int(input("Escolha o número do jogador: "))
    nome = jogadores_registados[escolha - 1]                 # converte o número visto (1..n) no índice (0..n-1)
    print(Fore.GREEN + f"Bem-vindo de volta, {nome}!")
    return nome                                              # devolve o nome para o menu saber quem está ativo


def criar_jogador():
    """Pede um nome novo, garante que não está repetido e guarda-o. Devolve o nome criado."""
    titulo_esquerdo(Fore.LIGHTCYAN_EX, "| CRIAR UTILIZADOR |", "—")



# Ciclo que só termina quando o nome introduzido for válido (o return é a saída)
    while True:
        nome = input("Nome de utilizador (3 a 20 caracteres): ").strip()        # strip tira espaços à volta

        if len(nome) < 3 or len(nome) > 20:
            print(Fore.RED + "O nome tem de ter entre 3 e 20 caracteres.")
            continue                        # volta a pedir o nome




        # Validação de nome repetido: percorre a lista a comparar em minúsculas,
        # para "Ana" e "ana" contarem como o mesmo jogador
        repetido = False
        for existente in jogadores_registados:
            if existente.lower() == nome.lower():
                repetido = True
                break


            # volta a pedir o nome
        if repetido:
            print(Fore.RED + "Já existe um jogador com esse nome. Escolha outro.")
            continue


             # Nome válido e único: guarda na lista e devolve-o
        jogadores_registados.append(nome)
        print(Fore.GREEN + f"Jogador '{nome}' criado com sucesso!")
        return nome


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
    

    escolha = int(input("Escolha uma opção (1 ou 2): "))

    if escolha == 1:
            nome = escolher_jogador()
    else:
            nome = criar_jogador()

    if nome is not None:
        return nome
        # Se não havia jogadores, volta ao menu de utilizadores

jogadores()