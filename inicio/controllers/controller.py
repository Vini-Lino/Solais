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
    pass # parte "U" do CRUD com a temperatura de um bairro

def atualizar_arvores():
    pass # parte "U" do CRUD com a quantidade de árvores de um bairro

def deletar_bairro():
    pass # parte "D" do CRUD com o bairro em si
