""""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO

"""

notaa = float(input("Digite a sua nota A:\n"))
notab = float(input("Digite a sua nota B:\n"))

media = float(notaa + notab) / 2

if media >= 7:
    print("Sua media foi {}. Voce esta APROVADO!".format(media))
elif media >= 5 and media <= 6.9:
    print("Sua media foi {}. Voce esta em RECUPERACAO!".format(media))
else:
    print("Sua media foi {}. Voce esta REPROVADO!".format(media))
