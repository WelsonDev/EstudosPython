"""
faca um programa que leia o valor
de um produto e calcule o valor
com 5% de desconto

"""
produto = float(input('Digite o valor do seu produto: R$ '))
desconto = (produto * 5) / 100

print('O Desconto no produto foi de R$ {:.2f}, com o Desconto ele vai custar: R$ {:.2f}'
      .format(desconto, produto - desconto))
