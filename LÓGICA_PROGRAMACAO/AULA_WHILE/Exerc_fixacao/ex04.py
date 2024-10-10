# Exercicio 4 - Escreva um programa que inicie uma contagem regressiva a
# partir de um número fornecido pelo usuário até zero,
# exibindo cada número na tela
num = int(input('Digite um número para a contagem regressiva:  '))

while num >= 1:
    print(num)
    num -= 1
print('FOGO')
