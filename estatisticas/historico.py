#Histórico
"""historico.py - Historico de partidas do utilizador (RF7 / RF8).
Regista cada partida (jogo, jogador, data, pontuação)
e premite consultar todas as partidas ou filtar por jogo / jogador.
"""

import csv
import os
from datetime import datetime
from pyclbr import Class

""" estas 3 linhas de codigo servem para: 
7. Trabalhar com ficheiros CSV (ficheiro que armazenam dados organizados em tabelas)
8. Interage com o sistema operativo (verifica se um ficheiro existe, cria ficheiros, etc.)
9. Trabalha com as datas e horas
"""


# Raiz do projeto
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# A linha 19 serve para obter o caminho da pasta onde está guardado o ficheiro Python atual.


class Partida:
    
    """Classe que representa uma partida de jogo, 
    num determinado jogo e com um determinado jogador, data e pontuação.
    """

def __init__(self, jogo, jogador, data, pontuacao):
            self.jogo = jogo
            self.jogador = jogador
            self.data = data
            self.pontuacao = int(pontuacao)

def get_jogo(self):
                return self.__jogo

def get_jogador(self):
                return self.__jogador

def get_pontuacao(self):
                return self.__pontuacao

def get_data(self):
                return self.__data

"""Estas linhas de codigo servem para definir a classe Partida, que representa uma partida de jogo. 
A classe tem um construtor (__init__) que recebe os parâmetros jogo, jogador, data e pontuação, 
e os armazena como atributos da instância. 
Além disso, existem métodos get_jogo, get_jogador, get_pontuacao e get_data que 
retornam os valores dos atributos correspondentes.  
"""