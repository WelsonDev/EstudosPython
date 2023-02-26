""""
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado.
"""

diault = int(input('Dias Alugado: '))
kmper = float(input('Digite o Kms percorridos: '))
total = (diault * 60) + (kmper * 0.15)

print('A valor total do alugel foi: R$ {}'.format(total))
