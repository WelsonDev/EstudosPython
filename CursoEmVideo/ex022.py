"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todos (sem considerar espaços.
- Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite seu nome'))

print('Esse e seu nome em maiusculo, {}'.format(nome.upper()))
print('Seu nome possui {} letras'.format(len(nome.strip())))
print('Seu primeiro nome possui {} letras'.format(int(nome.find(" "))))
