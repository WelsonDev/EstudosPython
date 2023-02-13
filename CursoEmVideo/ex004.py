"""
Faca um programa que leia algo pelo teclado
e mostre na tela o seu tipo e todas as
informacoes possiveis.
"""

valor = input('Digite um valor\n')
print('O Valor digitado foi: \n {}'.format(valor))
if valor.isnumeric() == True:
    print('O valor digitado e numerico:')
else:
    print(type(valor))
