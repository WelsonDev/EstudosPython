""""
044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros

"""
valorproduto = float(input("Digite o valor do produto:\n"))

formapgto = int(input("1 - A vista em dinheiro:\n" 
                      "2 - A vista no cartao de credito:\n"
                      "3 - ate 2x no cartao:\n"
                      "4 - Maior que 3x no cartao:\n"

                      ))
print(formapgto)
if formapgto == 1:
    valorproduto = valorproduto - (valorproduto * 10 /100)
    formapgto = "A Vista"
elif formapgto == 2:
    valorproduto = valorproduto - (valorproduto * 5 /100)
    formapgto = "A vista no credito"
elif formapgto == 3:
    valorproduto = valorproduto - (valorproduto * 20 / 100)
    formapgto = "Em 2x no credito"

print("A forma de pagamento selecionada foi,{} e o valor do produto ficou em {}".format(formapgto,valorproduto))

