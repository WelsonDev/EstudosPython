""""

Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

"""

distancia = int(input('Digite a distancia em kilometros da sua viagem\n'))

if distancia <= 200:
    print('O valor da passagem e R$ {:.2f}'.format(distancia * 0.50))
else:
    print('O valor da passagem e R$ {:.2f}'.format(distancia * 0.45))
