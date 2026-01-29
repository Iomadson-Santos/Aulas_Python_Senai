import getpass
def validar_senha(senha):
    if len (senha) >=8:
        print("Senha válida.")
        return True
    else:
        print("Senha inválida.")
        return False
    
def cadastro_terminal():
    usuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite uma senha de 8 digitos ou mais: ")
    while not validar_senha(senha):
        senha = input("Digite uma senha de 8 digitos ou mais: ")
    print("Cadastro realizado com sucesso!")
    
cadastro_terminal()