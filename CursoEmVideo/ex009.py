"""
faca um programa que leia um numero qualque
e mostre sua tabuada
"""

number = int(input('Digite um nemero e veja a tabuada:\n'))
numerador = 1
resultado = int

print('-' * 20)

for numerador in range(10):
    if numerador < 10:
        numerador += 1
        resultado = number * numerador
    print("{} x {:2} = {:2}" .format(number, numerador, resultado))
else:
    print('-' * 20)
