# from adivinha_o_numero import adivinha_o_numero
# from jogos.pedra_papel_tesoura import pedra_papel_tesoura
# from jogo_da_forca import jogo_da_forca

def match_case(opcao):
    match opcao:
        case 1:
            print("1")
            # adivinha_o_numero()
        case 2:
            print("2")
            # pedra_papel_tesoura()
        case 3:
            print("3")
            # jogo_da_forca()
        case 0:
            print("Saiste")
