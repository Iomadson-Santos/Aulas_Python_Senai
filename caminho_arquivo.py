nome = input("Digite um nome: ")
idade = int(input("Digite sua idade: "))
email= input("Digite um email: ")

with open("./pessoa.txt", "a") as arquivo:
    arquivo.write(f"Nome:{nome:<15} | Idade: {idade:<4} | E-MAIL:{email:<20}\n")

    #sqlalchemy
    #sqlite