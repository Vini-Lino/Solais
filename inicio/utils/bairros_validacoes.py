import os
currentdir = os.path.dirname(__file__)
path_db = os.path.join(currentdir, "..", "database", "bairros.txt")

def validar_nome_bairro():
    pass # um bairro não pode ter números ou simbolos especiais no nome, faça um código que faça com que apenas nomes com letras do alfabeto sejam válidos. Assim como um email, um bairro não pode ter o mesmo nome que outro bairro, implemente isso no código

def validar_temperatura():
    pass # a temperatura será definida por um número entre -70 à 70 (provavelmente nunca chegaria aos extremos, mas deixe essa faixa como válido mesmo assim), faça um código que faça com que apenas números (e não letras ou símbolos especiais) sejam válidos

def validar_numero_arvores():
    pass # essa parte do código é destinada para o número de árvores no bairro, aceitar somente números INTEIROS, sem letras, caracteres especiais, nem números negativos (como -10) ou/e quebrados (como 5,4), não tem como existirem árvores negativas ou pela metade


# Sei que o projeto seria sobre a gente intervir nas ilhas de calor, com soluções e intervenções, mas não dá pra implementar isso aqui pelo menos por agora,
# então o que eu estou pensando é que a gente faça só um CRUD mesmo, Criar, Read(seria ler, listar), Update(Seria atualizar, editar) e Deletar os bairros de Recife, com suas temperaturas e número de árvores,
# eu acredito que ficaria melhor em código pra a gente fazer assim, vamos em frente pessoal! :D
# quando o código de cima estiver pronto, pode remover esses comentários daqui de baixo, eles são só pra comunicar com quem está escrevendo os códigos (^-^)
