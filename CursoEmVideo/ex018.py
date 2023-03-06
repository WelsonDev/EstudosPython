""""
faca um programa que leia o angulo
qualquer e mostre na tela o valor
do seno, conseno e tangente desse
angulo
"""
from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do angulo: '))

seno = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))

print('O valor de seno e: {:.2f},\nO valor de consseno e: {:.2f},\nO valor da tangente e: {:.2f}'
      .format(seno, cos, tang))
