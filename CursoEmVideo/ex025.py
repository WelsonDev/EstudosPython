""""
Exercício Python 025: Crie um programa que leia
o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = str(input('Digite o nome da cidade')).strip()

# print(nome[::].upper() == 'SILVA')

print('Seu nome tem silva {}'.format('silva' in nome.lower()))
