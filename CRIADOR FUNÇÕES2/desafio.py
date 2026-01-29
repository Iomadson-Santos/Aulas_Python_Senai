cotação = 5.19
def converter_dolar_real(valor_dolar):
    return valor_dolar*cotação
def converter_real_dolar(valor_real):
    return valor_real/cotação

def menu():
    opcao = input("[1] - converter em dolar\n[2] - converter em real\n[3] - Sair\n Selecione uma opção:")
    if opcao == "1":
        valor1=float(input("Digite o valor em dolar: "))
        print(f"{converter_dolar_real(valor1):.2f}")
        

    elif opcao == "2":
        valor2=float(input("Digite o valor em real: "))
        print(f"{converter_real_dolar(valor2):.2f}")

    elif opcao == "3":
        print("Sair")

    else:
        print("Opção inválida")

menu()