""""
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

"""

salario = float(input("Digite o seu salario:\n"))

if salario < 1250:
    print("Seu salario com aumento e: {}".format(salario + 10))
else:
    print("Seu salario com aumento e: {}".format(salario * 15 / 100))
