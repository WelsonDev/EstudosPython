""""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
print("\033[30m=\033[m"*30)

escolha = int(input("Escolha a base que voce quer converter:\n 1: Binario\n 2: octal\n 3: hexadecinal\n"))

valor = int(input("Digite o valor que voce quer converter:\n"))

if escolha == 1:
    print("O valor digitado foi: {}, A conversao para binario e: {}".format(escolha, bin(valor)[2:]))
elif escolha == 2:
    print("O valor digitado foi: {}, A conversao para octal e: {}".format(escolha, oct(valor)[2:]))
elif escolha == 3:
    print("O valor digitado foi: {}, A conversao para hexadecimal e: {}".format(escolha, hex(valor)[2:]))
else:
    print("Opcao invalida!")
