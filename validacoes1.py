#nesse arquivo de validações, vai ser a parte onde vai validar se o nome, email, e senha são validos,
#crie um código que valide o nome, email e senha
#exemplo:
#exemplo@mail.com não é um email válido
#example@mail.com (válido, agora ele pede a senha)

def validar_nome(nome):

    nome = nome.replace(" ", "")

    return nome.isalpha() # estabelece critérios para tirar todos os espaços em branco do nome, e em seguida verifica se todos os caracteres são letras do alfabeto


def validar_email(email):

    email = email.strip()

    return "@" in email and "." in email # implementa um critério para remover espaços do início e fim do email e outro para verificar a ocorrência dos caracteres "@" e "." para ser um email válido


def validar_senha(senha):

    return len(senha) >= 6 # Implementa um critério de mínimo de 6 caracteres para validar a senha