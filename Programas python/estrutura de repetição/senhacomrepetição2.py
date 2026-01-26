usuario = input("Digite o nome de usúario: ")
senha =  input("Digite a senha diferente do nome de usúario: ")

while usuario == senha:
    print("Nome e senha de usúario invalidas coloque novamente")
    usuario = input("Digite o nome de usúario: ")
    senha =  input("Digite a senha diferente do nome de usúario: ")

print("Usúario registrado com sucesso")