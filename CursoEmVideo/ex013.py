""""
faca um programa que leia o salario
de um funcionario e calcule o
seu novo valor com 15% de aumento

"""

salario = float(input('Digite o valor do seu salario: R$ '))
aumento = (salario * 15) / 100

print('O Aumento do seu salario foi de R$ {:.2f}, Agora seu salario e: R$ {:.2f}'
      .format(aumento, salario + aumento))
