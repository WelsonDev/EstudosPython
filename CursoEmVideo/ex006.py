""""
crie um algoritmo que leia um e mostre
seu dobro e triplo da raiz quadrada

"""
import math

numero = float(input('Type a number:\n'))
dobraiz = math.sqrt(numero) * 2
triraiz = math.sqrt(numero) * 3
print('The Number given was: {}, The double of square root is: {:.3F} and it´s tripe is: {:.3F} '
      .format(numero, dobraiz, triraiz))
