""""
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""

n1 = int(input("Digite o primeiro numero"))
n2 = int(input("Digite o segundo numero"))
n3 = int(input("Digite o terceiro numero"))
""""
# Verifica qual numero e menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verifica qual numero e maior
maior = n1
if n2 > n1 and n2 > n3:
    menor = n2
if n3 > n1 and n3 > n2:
    menor = n3
    
print("O menor numero digitado foi: {}".format(menor))
print("O maior numero digitado foi: {}".format(maior))

"""
lista = [n1, n2, n3]
lista_ordenada = sorted(lista)

print('O menor número é {}'.format(lista_ordenada[0]))
print('O maior número é {}'.format(lista_ordenada[2]))


