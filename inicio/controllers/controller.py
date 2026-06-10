import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))

current_dir = os.path.dirname(__file__)

from ..utils.bairros_validacoes import * 

ARQUIVO = os.path.join(current_dir, "..", "database", "bairros.txt")


def salvar_bairros(bairro):
    
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        
        linha = (f"{bairro['nome']};{bairro['temperatura']};{bairro['arvores']}\n")

        arquivo.write(linha)


def carregar_bairros():

    bairros = []

    try:
        
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:
                
                dados = linha.strip().split(";")
                
                if len(dados) == 3:
                    bairro = {
                        "nome": dados[0],
                        "temperatura": dados[1],
                        "arvores": dados[2]
                    }
                    bairros.append(bairro)
    except FileNotFoundError:
    
        pass

    return bairros

def listar_bairros():
    bairros = carregar_bairros()

    if len(bairros) == 0:
        print("Nenhum bairro registrado no momento.")
        return

    print("\n--- Lista de Bairros ---")
    for bairro in bairros:
        print(f"Bairro: {bairro['nome']}")
        print(f"Temperatura: {bairro['temperatura']}°C")
        print(f"Quantidade de Árvores: {bairro['arvores']}")
        print("-" * 24)


def reescrever_bairros_database(bairros_lista):
    
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for b in bairros_lista:
            linha = f"{b['nome']};{b['temperatura']};{b['arvores']}\n"
            arquivo.write(linha)

def atualizar_nome_bairro(nome_antigo, nome_novo):
    bairros = carregar_bairros()
    for b in bairros:
        
        if b["nome"].lower() == nome_antigo.lower():
            b["nome"] = nome_novo 
            break
    reescrever_bairros_database(bairros) 

def atualizar_temperatura(nome_bairro, nova_temp):
    bairros = carregar_bairros()
    for b in bairros:
        if b["nome"].lower() == nome_bairro.lower():
            b["temperatura"] = nova_temp
            break
    reescrever_bairros_database(bairros)

def atualizar_arvores(nome_bairro, nova_qtd):
    bairros = carregar_bairros()
    for b in bairros:
        if b["nome"].lower() == nome_bairro.lower():
            b["arvores"] = nova_qtd
            break
    reescrever_bairros_database(bairros)

def deletar_bairro(nome_bairro):
    bairros = carregar_bairros()
    
    bairros_restantes = [b for b in bairros if b["nome"].lower() != nome_bairro.lower()]
    
    reescrever_bairros_database(bairros_restantes)