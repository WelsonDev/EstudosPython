""""
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

velociade = int(input('Digite a velociade que voce esta dirigindo:\n'))

multa = (velociade - 80) * 7

if velociade > 80:
    print('Voce esta acima da velociade permitida, Sua multa e de R$ {:.2f}'.format(multa))
else:
    print('Voce esta dentro do limite de velociade')
