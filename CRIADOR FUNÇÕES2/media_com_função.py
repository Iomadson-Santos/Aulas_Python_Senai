def media_valor(n1,n2,n3):
    media = (n1+n2+n3)/3
    return media >= 7

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

print(media_valor(n1,n2,n3))