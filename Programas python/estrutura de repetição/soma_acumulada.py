valor = int(input("Digite um valor: "))
acm = 0

while valor != 0:
    acm = acm + valor
    valor = int(input("Digite um valor (0 - Sair): "))
print(acm)