name = input("Enter your name: ")
while len(name) < 3:
    name = input("Your name needs to be longer than 3 characters: ")

age = int(input("Enter your age: "))
while age < 0 or  age > 150:
    age = int(input("Enter a valid age between 0 and 150!"))
    print(f"Your age is {age}")
              

salary = float(input("Enter your salary"))
while salary == 0:
    salary = float(input("Invalid salary, it needs to be greater than 0."))
    print(f"Your salary is R${salary:.2f}")

sex = input("Enter your gender: \
            \n (M - Masculino)\
            \n(F - Feminino)").upper()

while sex == "M" or sex == "F":
    sex = input("Sexo invalido")
    print("Seu sexo é")

marital_status = input("Enter marital status: (S - solterio)\
                       \n (C - Casado)\
                       \n (V - Viuvo)\
                       \n (D - Divorciado)").upper()
