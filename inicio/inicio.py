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
            while True:
                escolha = input("Escolha uma opção: ")
                if escolha == "0":
                    break
                else:
                    print("Opção inválida")

        elif opcao == "2":
            arbourb_menu() # ir para a tela de arborização urbana
            while True:
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
                    bairros_atuais = carregar_bairros()

                    if not bairros_atuais:
                        print("\nNenhum bairro registrado para alterar.")
                        input("Pressione ENTER para voltar...")
                        arbourb_menu()
                        continue

                    nome_alterar = input("Digite o nome do bairro que deseja alterar: ")

                    bairro_encontrado = False
                    for b in bairros_atuais:
                        if b["nome"].lower() == nome_alterar.strip().lower():
                            bairro_encontrado = True
                            nome_original = b["nome"]
                            break
                    
                    if not bairro_encontrado:
                        print(f"\nEste bairro não foi encontrado no sistema.")
                        input("Pressione ENTER para voltar...")
                        arbourb_menu()
                        continue

                    while True:
                        print(f"\n--- Alterando o bairro: {nome_original} ---")
                        print("1 - Alterar Nome")
                        print("2 - Alterar Temperatura")
                        print("3 - Alterar Quantidade de Árvores")
                        print("0 - Voltar")

                        op_alterar = input("Escolha o que deseja alterar: ")

                        if op_alterar == "0":
                            arbourb_menu()
                            break

                        elif op_alterar == "1":
                            novo_nome = input("Digite o novo nome do bairro: ")
                            while validar_nome_bairro(novo_nome) == False:
                                print("Nome inválido, deve conter apenas letras, ou o bairro já existe")
                                novo_nome = input("Digite o novo nome do bairro: ")

                            atualizar_nome_bairro(nome_original, novo_nome)
                            nome_original = novo_nome
                            print("\nNome atualizado com sucesso!")

                        elif op_alterar == "2":
                            nova_temp = input("Digite a nova temperatura: ")
                            while validar_temperatura(nova_temp) == False:
                                print("Temperatura inválida! deve conter um número de -70 a 70")
                                nova_temp = input("Digite a nova temperatura: ")

                            atualizar_temperatura(nome_original, nova_temp)
                            print("\nTemperatura atualizada com sucesso!")

                        elif op_alterar == "3":
                            novas_arvores = input("Digite a quantidade de árvores: ")
                            while validar_numero_arvores(novas_arvores) == False:
                                print("Número inválido! deve ser um número inteiro positivo")
                                novas_arvores = input("Digite a quantidade de árvores: ")

                            atualizar_arvores(nome_original, novas_arvores)
                            print("\nA quantidade de árvores foi atualizada com sucesso!")

                        else:
                            print("\nOpção inválida")

                elif escolha == "4":
                    bairros_atuais = carregar_bairros()

                    if not bairros_atuais:
                        print("Nenhum bairro encontrado para excluir")
                        input("Pressione ENTER para voltar...")
                        arbourb_menu()
                        continue

                    bairro_excluir = input("Digite um nome de um bairro para excluir: ")

                    bairro_encontrado = False
                    for b in bairros_atuais:
                        if b["nome"].lower() == bairro_excluir.strip().lower():
                            bairro_encontrado = True
                            nome_original = b["nome"]
                            break
                    
                    if not bairro_encontrado:
                        print(f"\nEste bairro não foi encontrado no sistema.")
                        input("Pressione ENTER para voltar...")
                        arbourb_menu()
                        continue

                    while True:
                        confirmation = input("Tem certeza que deseja excluir o bairro? (S/N): ").strip().upper()

                        if confirmation == "S":
                            deletar_bairro(nome_original)
                            print("\nBairro excluido com sucesso!")

                            arbourb_menu()
                            break
                        elif confirmation == "N":
                            print("\nAção cancelada")
                            arbourb_menu()
                            break
                        else:
                            print("\nOpção inválida, Por favor, digite S ou N")

                else:
                    print("Opção invalida")

        elif opcao == "3":
            relatorio_menu() # ir para a tela de relatórios de impacto
            while True:
                escolha = input("Escolha uma opção: ")
                if escolha == "0":
                    break
                elif escolha == "1":
                    listar_bairros()
                    input("Pressione ENTER para voltar...")
                    relatorio_menu()
                    continue

                elif escolha == "2":
                    bairros_atuais = carregar_bairros()

                    if not bairros_atuais:
                        print("\nNenhum bairro registrado no banco de dados.")
                        input("Pressione ENTER para voltar...")
                        relatorio_menu()
                        continue

                    termo_busca = input("Digite o nome do bairro que deseja buscar: ").strip()
                    bairro_encontrado = None

                    for b in bairros_atuais:
                        if b["nome"].lower() == termo_busca.lower():
                            bairro_encontrado = b
                            break

                    if bairro_encontrado:
                        nome = bairro_encontrado["nome"]
                        temp = float(bairro_encontrado["temperatura"])
                        arvores = bairro_encontrado["arvores"]

                        print(f"\n--- Relatório de Impacto: {nome} ---")
                        print(f"Temperatura Registrada: {temp}°C")
                        print(f"Quantidade de Árvores: {arvores}")
                        
                        if temp <= 0 or temp >= 40:
                            print("Status Climático: Temperatura Extrema")
                        else:
                            print("Status Climático: Estável")
                        
                        print("-" * 35)
                    else:
                        print(f"\nO bairro '{termo_busca}' não foi encontrado no sistema.")

                    input("\nPressione ENTER para voltar...")
                    relatorio_menu()

                else:
                    print("Opção inválida")

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