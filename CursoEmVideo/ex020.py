""""
o mesmo professor do desafio anterior
que sortear a ordem da apresentacao de
trabalhos dos alunos. faca um programa
que leia o nome dos quatros alunos e
mostre a ordem sorteada.

"""
from random import random, shuffle

alunos1 = str(input('Digite o nome dos alunos'))
alunos2 = str(input('Digite o nome dos alunos'))
alunos3 = str(input('Digite o nome dos alunos'))
alunos4 = str(input('Digite o nome dos alunos'))

lista = [alunos1, alunos2, alunos3, alunos4]
shuffle(lista)

print('a Sequencia de apresentacao sera: {}'.format(lista))
