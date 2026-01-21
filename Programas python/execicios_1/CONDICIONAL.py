nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))

if idade >= 18 :

    possui_carteira = input("Possui carteira de motorista?\n ( SIM /  NÃO) ")
    
    if possui_carteira == "SIM":
        print("Pode dirigi")
    else:
        print("Não pode dirigi")

else:
    print("Menor de idade")

print("Programa finalizado")