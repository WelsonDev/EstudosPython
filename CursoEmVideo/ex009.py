"""
faca um programa que leia um numero qualque
e mostre sua tabuada
"""

number = int(input('Digite um nemero e veja a tabuada:\n'))
numerador = 1
# resultado = number + numerador

for numerador in range(10):
    if numerador < 10:
        numerador += 1
        resultado = number * numerador
    print("{} x {} = {}" .format(number, numerador, resultado))
else:
    print('Fim')
