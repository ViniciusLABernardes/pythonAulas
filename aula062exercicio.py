nome_usuario = input("digite o nome de usuario ")
senha_usuario = input("digite a senha ")

loop = True

while senha_usuario == nome_usuario:
    print("a senha n pode ser igual o nome")
    senha_usuario = input("digite a senha: ")

print("cadastro feito")