""""
Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela a sua porção Inteira.
"""
import math


numero = float(input('Digite um numero real: '))
inteiro = math.trunc(numero)

print('O numero digitado foi: {}, seu numero inteiro e: {}'.format(numero, math.trunc(numero)))


