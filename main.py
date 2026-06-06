from controllers.controller import *
from views.menu_view import *

while True:

    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break

    elif opcao == "1":
        login_funcionario()
        break

    elif opcao == "2":

        nome = input("Digite o seu primeiro nome: ")
        
        while validar_nome(nome) == False:
            print("Nome inválido, deve conter apenas letras")
            nome = input("Digite o seu primeiro nome: ")

        email = input("Digite o seu email institucional: ")

        while validar_email(email) == False:
            email = input("Digite o seu email institucional: ")

        senha = input("Digite a sua senha: ")

        while validar_senha(senha) == False:
            print("A sua senha deve ter pelo menos 6 caracteres")
            senha = input("Digite a sua senha: ")

        funcionario = {
            "nome": nome,
            "email": email,
            "senha": senha
        }

        salvar_funcionario(funcionario)

        print("Funcionário salvo com sucesso!")

    elif opcao == "3":
        listar_funcionarios()

    elif opcao == "4":
        nome = input("Nome do funcionário: ")
        funcionario = buscar_funcionarios(nome)

        if funcionario:
            print("\nNome:", funcionario["nome"])
            print("Email:", funcionario["email"])
        else:
            print("Funcionário não encontrado")

    else:
        print("opção inválida!")
