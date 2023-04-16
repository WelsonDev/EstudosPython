""""
Exercioco aula 9
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.

"""
from random import randint

numero = int(input('Digite um numero de 0 a 5\n'))

sorteio = randint(0, 5)

if numero == sorteio:
    print('Valor digitado foi: {}, e o sorteado foi {}. Voce GANHOU!'.format(numero, sorteio))
else:
    print('Valor digitado foi: {}, O Sorteado foi: {}. Voce Perdeu!'.format(numero, sorteio))
