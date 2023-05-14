""""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""
import time as tm

idade = int(input("Digite a sua idade:\n"))

anohj = int(tm.strftime("%Y"))

categoria = anohj - idade

if categoria <= 9:
    print("Sua categoria e MIRIM.\n")
elif categoria <= 14:
    print("Sua categoria e INFANTIL.\n")
elif categoria <= 19:
    print("Sua categoria e JÚNIOR.\n")
elif categoria <= 25:
    print("Sua categoria e SÊNIOR.\n")
else:
    print("Sua categoria e MASTER.\n")
