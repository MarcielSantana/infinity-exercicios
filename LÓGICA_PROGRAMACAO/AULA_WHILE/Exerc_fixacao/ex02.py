# Exercicio 02 - Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue até que o usuário
# informe o valor válido.

nota = int(input('Digite uma nota entre 0 e 10: '))

while nota > 10:
    print('ERRO: Digite uma nota entre 0 e 10')
    nota = int(input('Digite uma nota entre 0 e 10: '))
print(f'ÓTIMO: Você digitou a nota "{nota}"')
