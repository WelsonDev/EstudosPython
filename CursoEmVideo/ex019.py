""""
um professor que sortear um
dos seus quatro alunos para
apagar o quadro. faca um programa
que ajude ele, lendo o nome
dele e escrevendo o nome do
escolhido.
"""
from random import choice
alunos1 = input('Digite o nome dos alunos')
alunos2 = input('Digite o nome dos alunos')
alunos3 = input('Digite o nome dos alunos')
alunos4 = input('Digite o nome dos alunos')

lista = [alunos1, alunos2, alunos3, alunos4]

print('O Aluno que vai apagar a losa e: {}'.format(choice(lista)))
