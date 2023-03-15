""""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""
nome = str(input('Digite seu nome'))
nome = nome.split()

cont = len(nome)

print('Seu primeiro nome e: {}'.format(nome[0]))
print('Seu ultimo nome e: {}'.format(nome[-1]))
