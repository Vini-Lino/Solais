import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))

current_dir = os.path.dirname(__file__)

from ..utils.validacoes import *

ARQUIVO = os.path.join(current_dir, "..", "database", "funcionarios.txt")


def login_funcionario():
    funcionarios = carregar_funcionarios()

    if not funcionarios:
        print("Erro: Nenhum funcionário registrado no sistema.")
        return None

    usuario_encontrado = None

    while True:
        type_email = input("Digite o seu email: ").strip()

        for funcionario in funcionarios:
            if funcionario["email"].lower() == type_email.lower():
                usuario_encontrado = funcionario
                break
        
        if usuario_encontrado:
            break
        else:
            print("Email não encontrado. Tente novamente.")

    while True:
        type_password = input("Digite a sua senha: ").strip()

        if type_password == usuario_encontrado["senha"]:
            print(f"\nBem Vindo(a), {usuario_encontrado["nome"]}!")
            return usuario_encontrado
        else:
            print("Senha incorreta. Tente novamente.")

def salvar_funcionario(funcionario):
    
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:

        linha = (
            f"{funcionario['nome']};"
            f"{funcionario['email']};"
            f"{funcionario['senha']}\n"
        )

        arquivo.write(linha)

def carregar_funcionarios():

    funcionarios = []

    try:

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                dados = linha.strip().split(";")

                if len(dados) == 3:
                    funcionario = {
                        "nome": dados[0],
                        "email": dados[1],
                        "senha": dados[2]
                    }

                    funcionarios.append(funcionario)

    except FileNotFoundError:
        pass

    return funcionarios

def listar_funcionarios():

    funcionarios = carregar_funcionarios()

    if len(funcionarios) == 0:
        print("Nenhum funcionário registrado")
        return

    for funcionario in funcionarios:

        print("\nNome:", funcionario["nome"])
        print("Email:", funcionario["email"])
        print("-" * 20)

def buscar_funcionarios(nome):

    funcionarios = carregar_funcionarios()

    for funcionario in funcionarios:

        if funcionario["nome"].lower() == nome.lower():
            return funcionario

    return None

def reescrever_database(funcionarios_lista):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for f in funcionarios_lista:
            linha = f"{f['nome']};{f['email']};{f['senha']}\n"
            arquivo.write(linha)

def atualizar_senha(email, nova_senha):
    funcionarios = carregar_funcionarios()

    for f in funcionarios:
        if f["email"] == email:
            f["senha"] = nova_senha
            break

    reescrever_database(funcionarios)

def deletar_conta(email):
    funcionarios = carregar_funcionarios()

    funcionarios_restantes = [f for f in funcionarios if f["email"] != email]

    reescrever_database(funcionarios_restantes)