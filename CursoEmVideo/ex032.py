""""

Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

ano = int(input('Digite o ano para verificar se e bissexto'))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto.')
else:
    print('Não é um ano bissexto.')
