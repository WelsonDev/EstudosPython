""""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

prinum = int(input("Digite o valor:\n"))
segnum = int(input("Digite o segundo valor\n"))

if prinum > segnum:
    print("O primeiro valor digitado: {}, e maior que o segundo valor digitado: {}".format(prinum, segnum))
elif segnum > prinum:
    print("O segundo valor digitado: {}, e maior que o primeiro valor digitado: {}".format(segnum, prinum))
else:
    print("Nao existe valor maior, os dois sao iguais!")
