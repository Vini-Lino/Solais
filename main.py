#Local onde vai ficar o projeto principal

try:
    from controllers.controller import *
    from views.menu_view import *
except Exception:
    # fallback stubs when controllers.controller is unavailable
    def validar_nome(name):
        return isinstance(name, str) and len(name.strip()) > 0

    def salvar_aluno(student):
        print("[warning] salvar_aluno não disponível. dados recebidos:", student)

    def update_nota(name):
        print(f"[warning] update_nota não disponível para: {name}")

    def listar_alunos():
        print("[warning] listar_alunos não disponível")

    def procurar_aluno(name):
        print(f"[warning] procurar_aluno não disponível para: {name}")
        return None

    def checar_status(media, presence):
        print(f"[warning] checar_status não disponível. media={media}, presence={presence}")
        return None

    def listar_aprovados():
        print("[warning] listar_aprovados não disponível")

    def listar_reprovados():
        print("[warning] listar_reprovados não disponível")

try:
    from views.menu_view import *
except Exception:
    # fallback stub for menu
    def exibir_menu():
        print("\n=== MENU ===\n1 - Cadastrar aluno\n2 - Atualizar nota\n3 - Listar alunos\n4 - Consultar aluno\n5 - Listar aprovados\n6 - Listar recuperação/reprovados\n0 - Sair\n")

while True:
    exibir_menu()
    option = input("escolha uma opção: ")
    if option == "1":
        name = str(input(f"nome: "))
        while validar_nome(name) == False:
            print(f"nome inválido")
            name = str(input(f"nome: "))
        age = int(input(f"idade: "))
        course = str(input(f"turma: "))
        presence = float(input(f"frequência: "))
        nota1 = float(input(f"nota: "))
        nota2 = float(input(f"nota: "))
        nota3 = float(input(f"nota: "))
        student = {
            "name": name,
            "age": age,
            "course": course,
            "presence": presence,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
        }
        salvar_aluno(student)
        print(f"aluno cadastrado")
    elif option == "2":
        name = str(input(f"nome do aluno: "))
        update_nota(name)
    elif option == "3":
        listar_alunos()
    elif option == "4":
        name = str(input(f"nome do aluno: "))
        student = procurar_aluno(name)
        if student:
            media = (student.get("nota1", 0) + student.get("nota2", 0) + student.get("nota3", 0)) / 3
            status = checar_status(
                media,
                student["presence"]
            )
        else:
            print(f"aluno não encontrado")
    elif option == "5":
        print(f"\n=== APROVADOS ===")
        listar_aprovados()
    elif option == "6":
        print(f"\n=== RECUPERAÇÃO/REPROVADOS ===")
        listar_reprovados()
    elif option == "0":
        print(f"encerrando...")
        break
    else:
        print(f"opção inválida")