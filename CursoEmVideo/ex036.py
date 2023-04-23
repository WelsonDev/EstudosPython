""""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.


"""
print("\033[30m=\033[m"*30)
print("Bem vindo ao financiamento python")
print("\033[30m=\033[m"*30)

vlcasa = float(input("Digite o valor da casa que voce quer comprar:\n"))
tpagamento = int(input("Em quanto tempo voce quer pagar o seu financiamento?\n")) * 12
vlsalario = float(input("Digite o valor do seu salario:\n"))
compsalario = vlsalario * 30 / 100
vlparcelea = vlcasa / tpagamento
print("\033[30m=\033[m"*30)


if vlparcelea > compsalario:
    print("O valor da parcela: {:.2f} e maior que 30% do seu salario {:.2f}, financiamento negado"
          .format(vlparcelea, compsalario))
else:
    print("O valor da parcela: {:.2f} e menor que 30% do seu salario: {:.2f}, financiamento aprovado"
          .format(vlparcelea, compsalario))

print("\033[30m=\033[m"*30)
