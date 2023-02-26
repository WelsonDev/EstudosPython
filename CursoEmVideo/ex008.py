"""
escreva um programa que leia um valor
em metros e o exiba convertido em
centimetros e milimetros
"""

metro = float(input('Digite o valor em metros: \n'))
centimetro = metro * 100
milimetro = metro * 1000

print('o Valor digitado em Centimetros e: {} e em milimetros e: {}'
      .format(centimetro, milimetro))
