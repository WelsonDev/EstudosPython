""""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime as tm

#anonasc = int(input("Digite o ano que voce nasceu:\n"))

anohj = tm.strftime("%d/%m/%y")

print("{}".format(anohj))


