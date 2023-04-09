""""
Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

numero = int(input('Digite um numero para saber se e par ou impar:\n'))

if numero % 2 == 0:
    print('O numero digitado {} e par'.format(numero))
else:
    print('O Numero digitado {} e impar'.format(numero))
