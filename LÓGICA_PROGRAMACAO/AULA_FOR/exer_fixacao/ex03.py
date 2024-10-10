# Exercicio 3 - Escreva um programa que escreva a tabuada de 7 de (1 a 10)

for num in range(1, 11):
    print(f'7 x {num} = {7 * num}')


# outra solução:
num = int(input('Qual número você quer saber a tabuada? '))
numero = 1
while numero <= 10:
    print(f'{num} * {numero} = {num * numero}')
    numero += 1
