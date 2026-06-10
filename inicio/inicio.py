import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))

current_dir = os.path.dirname(__file__)

from login.login import iniciar_sistema_login
from .views.menu_view import inicio_menu
from .views.config import *
from .controllers.controller import *
from login.controllers.controller import atualizar_senha, deletar_conta
from login.utils.validacoes import validar_senha
from inicio.views.ilhascalor import ilhas_menu
from inicio.views.arbourb import arbourb_menu
from inicio.views.rel_imp import relatorio_menu

def iniciar_inicio(usuario_encontrado):
    while True:

        inicio_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Deslogando...")
            break

        elif opcao == "1":
            ilhas_menu() # ir para a tela de ilhas de calor
            while True: # continuar daqui se tiver mais alguma opção de escolha
                escolha = input("Escolha uma opção: ")
                if escolha == "0":
                    break
                else:
                    print("Opção inválida")

        elif opcao == "2":
            arbourb_menu() # ir para a tela de arborização urbana
            while True: # continuar daqui se tiver mais alguma opção de escolha
                escolha = input("Escolha uma opção: ")
                if escolha == "0":
                    break
                elif escolha == "1":

                    nome_bairro = input("Digite o nome do bairro: ")

                    while validar_nome_bairro(nome_bairro) == False:
                        print("Nome inválido, deve conter apenas letras, ou o bairro já existe")
                        nome_bairro = input("Digite o nome do bairro: ")

                    temperatura = input("Digite a temperatura do bairro: ")

                    while validar_temperatura(temperatura) == False:
                        print("Temperatura inválida! deve conter um número de -70 a 70")
                        temperatura = input("Digite a temperatura do bairro: ")

                    arvores = input("Digite o número de árvores: ")

                    while validar_numero_arvores(arvores) == False:
                        print("Número inválido! deve ser um número inteiro positivo")
                        arvores = input("Digite o número de árvores: ")

                    bairro = {
                        "nome": nome_bairro,
                        "temperatura": temperatura,
                        "arvores": arvores
                    }

                    salvar_bairros(bairro)
                    print("Bairro salvo com sucesso!")
                    arbourb_menu()

                elif escolha == "2":
                    listar_bairros()
                    arbourb_menu()
                    
                elif escolha == "3":
                    pass # Alterar bairros, primeiro perguntar qual bairro deseja alterar, depois qual informação do bairro, nome, temperatura, ou quantiade de árvores
                elif escolha == "4":
                    pass # Excluir bairros, primeiro perguntar qual bairro deseja excluir, com confirmação de S/N
                else:
                    print("Opção invalida")

        elif opcao == "3":
            relatorio_menu() # ir para a tela de relatórios de impacto
            while True: # continuar daqui se tiver mais alguma opção de escolha
                escolha = input("Escolha uma opção: ")
                if escolha == "0":
                    break
                else:
                    print("Opção inválida") # por enquanto não decidi ainda sobre essa parte, e agora estou pensando se sequer vai existir uma tela dedicada pra o relatório se ele só faz listar as informações dos bairros o que a opção 2 já pode fazer... então por enquanto, ignora isso aqui até ter partes desse CRUD funcionando

        elif opcao == "4":
            config_conta(usuario_encontrado)

            while True:
                opcoes = input("Escolha uma opção: ")
                if opcoes == "0":
                    break
                elif opcoes == "1":
                    nova_senha = input("Digite a nova senha: ")

                    while validar_senha(nova_senha) == False:
                        print("A sua senha deve ter pelo menos 6 caracteres")
                        nova_senha = input("Digite a nova senha: ")
                    
                    usuario_encontrado["senha"] = nova_senha

                    atualizar_senha(usuario_encontrado["email"], nova_senha)
                    print("\nSenha atualizada com sucesso!")
                    break

                elif opcoes == "2":
                    while True:
                        confirmacao = input("Tem certeza que deseja apagar sua conta? (S/N): ").strip().upper()
                    
                        if confirmacao == "S":
                            deletar_conta(usuario_encontrado["email"])
                            print("\nConta apagada com sucesso. Você foi deslogado.")

                            return
                        elif confirmacao == "N":
                            print("\nAção cancelada")
                            config_conta(usuario_encontrado)
                            break
                        else:
                            print("\nOpção inválida, Por favor, digite S ou N")

                else:
                    print("Opção inválida")

        else:
            print("Opção inválida")