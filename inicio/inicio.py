from login.login import iniciar_sistema_login
from .views.menu_view import inicio_menu
from .controllers.controller import *

def iniciar_inicio(usuario_logado):
    while True:

        inicio_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Deslogando...")
            break

        elif opcao == "1":
            pass # ir para a tela de ilhas de calor

        elif opcao == "2":
            pass # ir para a tela de arborização urbana

        elif opcao == "3":
            pass # ir para a tela de relatórios de impacto

        else:
            print("Opção inválida")