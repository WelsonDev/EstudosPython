""""
Faça um programa que leia uma frase
pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição
ela aparece a última vez.
"""
frase = str(input('Digite uma frase: \n')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A Primeira letra A apareceu na posisao {}'.format(frase.find('A')+1))
print('A Ultima letra A apareceu na posisao {}'.format(frase.rfind('A')+1))
