""""
 Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""

# print("=\033[0:33:44m" * 20)
print("=" * 20)

n1 = float(input("Digite o primeiro segmento: "))
n2 = float(input("Digite o segundo segmento: "))
n3 = float(input("Digite o terciro segmento: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Os Segmentos acima podem formar um triangulo ", end="")
    if n1 == n2 == n3:
        print("Equilatero")
    elif n1 != n2 != n3 != n1:
        print("Escaleno")
    else:
        print("Isosceles")
else:
    print("Os segmetos acima nao podem formar um triangulo")
