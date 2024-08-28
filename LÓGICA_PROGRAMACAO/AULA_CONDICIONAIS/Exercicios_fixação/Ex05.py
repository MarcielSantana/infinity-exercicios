# Escreva um programa que verifica se dois números digitados pelo usuário são diferentes entre si, 
# e imprima o resultado.
num1 = int(input('Digite o PRIMEIRO número: '))
num2 = int(input('Digite o SEGUNDO número: '))

if num1 != num2:
    print(f'Os números {num1} e {num2} são DIFERENTES')
else:
    print(f'Os números {num1} e {num2} são IGUAIS')
