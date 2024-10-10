# Exercicio 01 - crie um programa que leia duas notas e tire a média delas.
# O programa só deverá aceitar notas entre 0 e 10.


num1 = float(input('Digite a primeira nota (entre 0 e 10): '))

while num1 < 0 or num1 > 10:
    num1 = float(input('NOTA INVÁLIDA. Digite a primeira nota (entre 0 e 10): '))
 
num2 = float(input('Digite a segunda nota (entre 0 e 10): '))
while num2 < 0 or num2 > 10:
    num2 = float(input('NOTA INVÁLIDA. Digite a segunda nota (entre 0 e 10): '))


media = (num1 + num2) / 2
print(f'A media entre {num1} e {num2} é {media}')
