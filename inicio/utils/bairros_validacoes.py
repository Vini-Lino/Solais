import os
currentdir = os.path.dirname(__file__)
path_db = os.path.join(currentdir, "..", "database", "bairros.txt")

def validar_nome_bairro(nome):
    nome_sem_espaco = nome.replace(" ", "")
    if not nome_sem_espaco.isalpha():
        return False
    try:
        with open(path_db, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if len(dados) > 0:
                    nome_banco = dados[0].strip()

                    if nome.strip().lower() == nome_banco.lower():
                        return False
    except FileNotFoundError:
        pass

    return True

    return nome.isalpha()

def validar_temperatura(temp):
    try:
        temp_num = float(temp)
        if temp_num >= -70 and temp_num <= 70:
            return True
        return False
    except ValueError:
        return False

def validar_numero_arvores(numero):
   try:
        num_int = int(numero)
        if num_int >= 0:
            return True
        return False
   
   except ValueError:
       return False


# Sei que o projeto seria sobre a gente intervir nas ilhas de calor, com soluções e intervenções, mas não dá pra implementar isso aqui pelo menos por agora,
# então o que eu estou pensando é que a gente faça só um CRUD mesmo, Criar, Read(seria ler, listar), Update(Seria atualizar, editar) e Deletar os bairros de Recife, com suas temperaturas e número de árvores,
# eu acredito que ficaria melhor em código pra a gente fazer assim, vamos em frente pessoal! :D
# quando o código de cima estiver pronto, pode remover esses comentários daqui de baixo, eles são só pra comunicar com quem está escrevendo os códigos (^-^)
