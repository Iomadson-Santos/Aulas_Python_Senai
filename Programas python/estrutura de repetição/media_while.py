valor = int(input("Digite um valor: "))
contador = 0
acm = 0

while  valor != -1:
    acm = acm+valor
    valor = int(input("Digite um valor (-1 - Sair): "))
    contador = contador+1
print(acm/contador)