valor_total =float(input("Digite o valor total: "))
valor_porcentagem =float(input("Digite a porcentagem desejada: "))

valor_parte = valor_total*(valor_porcentagem/100)

print(f"{valor_porcentagem}% de {valor_total} é {valor_parte}")