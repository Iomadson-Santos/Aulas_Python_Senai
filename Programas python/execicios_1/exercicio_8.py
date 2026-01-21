#calculadora salario#
valor_hora = float(input("Digite o valor da sua hora trabalhada: "))
horas_trabalhada_mes = int(input("Digite a quantidade de horas trabalhada no mês: "))

salario = valor_hora*horas_trabalhada_mes

print(f"O seu salário é: {salario:.2f}")