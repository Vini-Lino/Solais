def config_conta(usuario_encontrado):
    print("\nConfigurações da sua conta:")
    print(f"Nome: {usuario_encontrado['nome']}")
    print(f"Email: {usuario_encontrado['email']}")
    print("\n1 - mudar a senha")
    print("2 - apagar a conta")
    print("0 - menu anterior")