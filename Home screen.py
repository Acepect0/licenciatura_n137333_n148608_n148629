"""
Menu Principal do Projeto Final 

@description: menu inicial do projeto final da unidade curricular de Fundamentos de programação
@version: 0.0.1v
@author: Alexandre Rogado, nº137333 - Martim Soares, nº148608 - Rúben Gaspar, nº148629
"""

from colorama import Fore, Back, Style, init
import random
import shutil
from jogos import main

init(autoreset=True)

def menu():
    # A mensagem correspondente á escolha do utilizador
    print("Escolha um utlizador existente")
    print("Crie um novo utilizador")
