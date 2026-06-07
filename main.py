from login.login import iniciar_sistema_login
from inicio.inicio import iniciar_inicio

if __name__ == "__main__":
    while True:
        usuario_encontrado = iniciar_sistema_login()

        if usuario_encontrado:
            print(f"Logged in as {usuario_encontrado['nome']}")
            iniciar_inicio(usuario_encontrado)

        else:
            print("encerrando o sistema...")
            break