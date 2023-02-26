"""
faca um programa que leia a altura e
largura de uma parede em metros
e calcule sua area e a quantidade de
tinta necessaria para pinta-la,
sabendo que 1 litro de tinta
pinta uma area de 2m
"""

largura = float(input('Digite a largura: '))
altura = float(input('Digite largura: '))
area = float(largura * altura)
qtd_tinta = area / 2

print('A area total e: {:.3f}m, sera necessario {:.2f} litros de tinta para pintar todas as paredes'
      .format(area, qtd_tinta))
