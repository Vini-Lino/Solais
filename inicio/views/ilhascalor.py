import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.dirname(__file__)

from ..controllers.controller import carregar_bairros

def ilhas_menu():
    bairros = carregar_bairros()

    total_temp = 0
    total_arvores = 0
    zonas_resfriadas = 0
    zonas_criticas = 0
    qnt_bairros = len(bairros)

    if qnt_bairros > 0:
        for bairro in bairros:
            temp = float(bairro["temperatura"])
            arvores = int(bairro["arvores"])

            total_temp += temp
            total_arvores += arvores

            if temp < 30:
                zonas_resfriadas += 1

            if temp > 40:
                zonas_criticas += 1

            media_temp = total_temp / qnt_bairros
    else:
        media_temp = 0

    print("\n--- Informações sobre as ilhas de calor no Recife ---")
    print(f"Temperatura média: {media_temp:.2f}ºC")
    print(f"Árvores (Total): {total_arvores}")
    print(f"Zonas resfriadas (< 30ºC): {zonas_resfriadas} bairros")
    print(f"Zonas críticas (> 40ºC): {zonas_criticas} bairros")
    print("0 - menu anterior")