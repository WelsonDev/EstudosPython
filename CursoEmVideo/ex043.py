""""
 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
 e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida

"""

altura = int(input("Digite sua altura:\n"))
peso = int(input("Digite seu peso:\n"))

imc = (peso / altura) ** 2

if imc <= 18.5:
    print("seu IMC e :{}. Voce esta abaixo do Peso".format(imc))
elif imc <= 25:
    print("seu IMC e :{}. Voce esta com o peso ideal".format(imc))
elif imc <= 30:
    print("seu IMC e :{}. Voce esta com sobrepeso".format(imc))
elif imc <= 40:
    print("seu IMC e :{}. Voce esta com obesidade".format(imc))
else:
    print("seu IMC e :{}. Voce esta com obesidade morbida".format(imc))


