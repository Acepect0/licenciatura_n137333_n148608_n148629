# from adivinha_o_numero import adivinha_o_numero
# from jogos.pedra_papel_tesoura import pedra_papel_tesoura
# from jogo_da_forca import jogo_da_forca
from menu.funcoes_visuais import ecra_cheio, esperar, tela
from menu.manutencao import em_manutencao
from menu.barra_transicao_bem_sucedida import ecra_barra_suc
from menu.barra_transicao_mal_sucedida import ecra_barra_mal

def match_case(opcao):
    match opcao:
        case 1:
            ecra_barra_mal()
            em_manutencao()
            # adivinha_o_numero()
        case 2:
            ecra_barra_mal()
            em_manutencao()
            # pedra_papel_tesoura()
        case 3:
            ecra_barra_mal()
            em_manutencao()
            # jogo_da_forca()
        case 0:
            print("Voltando ao ecrã inicial..")
