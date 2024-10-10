# Exercicio 7 - Escreva um programa que verifica se um número é divisil por 5.
# Se for divisivel, imprima "O número é divisivel por 5"

num = int(input('Digite um número e veja se é divisivel por 5: '))

if num % 5 == 0:
    print(f'O número {num} é divisivel por 5')
else:
    print(f'O número {num} NÃO é divisivel por 5')