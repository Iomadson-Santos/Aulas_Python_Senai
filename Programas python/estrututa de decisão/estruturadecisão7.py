n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1<n2:
    menor = n1

else:
    menor=n2

if n3 < menor: 
    menor = n3

print(f"O menor número é {menor}")