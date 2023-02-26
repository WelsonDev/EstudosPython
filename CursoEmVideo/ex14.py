"""
 Escreva um programa que converta uma temperatura digitando em
 graus Celsius e converta para graus Fahrenheit.

"""
celsius = float(input('Digite o graus celsius: '))
# fahrenheit = float(celsius * 1.8) + 32
fahrenheit = float((celsius * 9)/5) + 32
# °F = °C × 1,8 + 32
print('A conversao de {}ºC para fahrenheit e {}ºF'.format(celsius, fahrenheit))

