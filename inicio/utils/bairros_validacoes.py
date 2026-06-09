import os
currentdir = os.path.dirname(__file__)
path_db = os.path.join(currentdir, "..", "database", "bairros.txt")

def validar_nome_bairro(nome):
    pass # um bairro não pode ter números ou simbolos especiais no nome, faça um código que faça com que apenas nomes com letras do alfabeto sejam válidos. Assim como um email, um bairro não pode ter o mesmo nome que outro bairro, implemente isso no código

def validar_temperatura(temp):
    if temp >= -70 and temp <= 70:
        return True
    return False

def validar_numero_arvores(numero):
   if type(numero) != int:
        return False
   if numero < 0:
        return False
   return True


# Sei que o projeto seria sobre a gente intervir nas ilhas de calor, com soluções e intervenções, mas não dá pra implementar isso aqui pelo menos por agora,
# então o que eu estou pensando é que a gente faça só um CRUD mesmo, Criar, Read(seria ler, listar), Update(Seria atualizar, editar) e Deletar os bairros de Recife, com suas temperaturas e número de árvores,
# eu acredito que ficaria melhor em código pra a gente fazer assim, vamos em frente pessoal! :D
# quando o código de cima estiver pronto, pode remover esses comentários daqui de baixo, eles são só pra comunicar com quem está escrevendo os códigos (^-^)
