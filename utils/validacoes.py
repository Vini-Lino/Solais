import os
currentdir = os.path.dirname(__file__)
path_db = os.path.join(currentdir, "..", "database", "funcionarios.txt")

def validar_nome(nome):

    nome = nome.replace(" ", "")

    return nome.isalpha()


def validar_email(email):

    email = email.strip()

    if not email.endswith("@cesar.school") and len(email) > 13:
        print("Email inválido, o email deve finalizar com @cesar.school")
        return False

    with open(path_db, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            if len(dados) == 3:
                registered_email = dados[1].lower()

                if email == registered_email:
                    print("email já registrado!")
                    return False
    

    return email.endswith("@cesar.school") and len(email) > 13

def validar_senha(senha):

    return len(senha) >= 6 
