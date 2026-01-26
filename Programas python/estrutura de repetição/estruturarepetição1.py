nota = int(input("Digite uma nota: "))

while nota < 0 or  nota > 10:
     print("Sua nota é invalida coloque uma nota válida")
     nota= int(input("Digite uma nota: "))

print(f"Sua nota é {nota}")