from validations.validacoes import *

ARQUIVO = "DataBase/funcionarios.txt"


def salvar_funcionario(funcionario):
    
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:

        linha = (
            f"{funcionario['nome']};"
            f"{funcionario['email']}"
            f"{funcionario['senha']}"
        )

        arquivo.write(linha)

def carregar_funcionarios():

    funcionario = []

    try:

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                dados = linha.strip().split(";")

                funcionario = {
                    "nome": dados[0],
                    "email": dados[0],
                    "senha": dados[0]
                }

                funcionario.append(funcionario)

    except FileNotFoundError:
        pass

    return funcionario

def listar_funcionarios():

    funcionarios = carregar_funcionarios()

    if len(funcionarios) == 0:
        print("Nenhum funcionário registrado")
        return

    for funcionario in funcionarios:

        print("\nNome:", funcionario["nome"])
        print("email:", funcionario["email"])

def buscar_funcionario(nome):

    funcionarios = carregar_funcionarios()

    for funcionario in funcionarios:

        if funcionario["nome"].lower() == nome.lower():
            return funcionario

    return None