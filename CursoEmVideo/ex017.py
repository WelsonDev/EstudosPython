""""
faca um programa que leia o comprimento
do cateto adjacente de um triangulo
retangulo, calcule e mostre o
comprimento da hipotenusa
"""
import math

cata = float(input('Digite o valor do cateto adjacente'))
cato = float(input('Digite o valor do cateto oposto'))

hipo = (cata ** 2 + cato ** 2) ** 4 (1/2)
hipo2 = math.hypot(cato, cata)
print('{}'.format(hipo))
print('{}'.format(hipo2))

