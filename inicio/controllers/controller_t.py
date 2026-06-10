import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))

current_dir = os.path.dirname(__file__)

from ..utils.bairros_validacoes import *

ARQUIVO = os.path.join(current_dir, "..", "database", "bairros.txt")

def salvar_bairros():
    pass # "salvar" como em "criar" bairros com CRUD

def carregar_bairros():
    pass # "carregar bairros na lista de bairros no banco de dados"

def listar_bairros():
    pass # listar os bairros criados... posso pensar se adiciono buscar bairros também, mas a esse ponto eu já estaria fazendo da tela relatórios mais inútil parando pra pensar...

def reescrever_bairros_database():
    pass # a esse ponto já da pra ver a inspiração no outro controller.py, vê o que ele faz e volta aqui

def atualizar_nome_bairro():
    pass # parte "U" do CRUD com o nome de um bairro

def atualizar_temperatura():
    temperatura = float(input("Digite a temperatura do bairro: "))
    resultado = validar_temperatura(temperatura)

    if resultado:
        print("Temperatura válida!")
    else:
        print("Temperatura inválida! O valor deve estar entre -70 e 70.")

def atualizar_arvores():
    entrada = input("Digite o número de árvores: ")
 
    if not entrada.isdigit():
        print("Inválido! Digite apenas números inteiros.")
    else:
        numero_arvores = int(entrada)
        resultado = validar_numero_arvores(numero_arvores)

        if resultado:
            print("Número de árvores válido!")
        else:
            print("Inválido! Não pode ser negativo.")

def deletar_bairro():
    pass # parte "D" do CRUD com o bairro em si
