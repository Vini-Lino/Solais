from login.login import iniciar_sistema_login

if __name__ == "__main__":
    usuario_encontrado = iniciar_sistema_login()

if usuario_encontrado:
    print("\nif you see this in the right place, we can follow from here!")
    print(f"Logged in as {usuario_encontrado["nome"]}")