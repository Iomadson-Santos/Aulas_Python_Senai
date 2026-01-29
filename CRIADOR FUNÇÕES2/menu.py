from soma_com_funções import soma
from par_or_impar import eh_par

def menu():
    opcao = input("[1] - Somar\n[2] - Verificação de Par\n[0] - Sair\n")

    if opcao == "1":
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        print(soma(valor1,valor2))

    elif opcao == "2":
        valor1 = int(input("Digite o valor que deseja verificar se é par: "))
        if eh_par(valor1):
            print("Par!")
        else:
            print("Ímpar!")

    elif opcao == "0":
        print("Sair")

    else:
        print("Opção inválida.")

menu()