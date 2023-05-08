""""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime as dt
import time as tm
anonasc = int(input("Digite o ano que voce nasceu:\n"))

anohj = int(tm.strftime("%Y"))
anoalist = anonasc + 16

if anohj <= anoalist:
    if (anoalist - anohj) < 0:
        print("Seu periodo de alistamento ja passo, Atraso de {} Ano".format(anoalist - anohj)*-1)
    else:
        print("Voce ainda tem {} ano(s) para fazer seu alistamento".format(anoalist - anohj))

    print("Ano e igual")
else:
    print("Ano nao e igual")

print("{}".format(anohj))


