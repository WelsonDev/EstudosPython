""""
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.

"""
print("=" * 20)

n1 = float(input("Digite o primeiro segmento: "))
n2 = float(input("Digite o segundo segmento: "))
n3 = float(input("Digite o terciro segmento: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Os Segmentos acima podem formar um triangulo: ")
else:
    print("Os segmetos acima nao podem formar um triangulo")
