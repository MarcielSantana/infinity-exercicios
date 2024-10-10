# Exercicio 6 - Escreva um programa que verifica a idade de uma pessoa e imprime em qual faixa etária
# ela se encontra.
idade = int(input('Qual sua idade? '))

if idade <= 11:
    print('Você é CRIANÇA')
elif idade >= 12 and idade <= 17:
    print('Você é ADOLESCENTE')
elif idade >= 18 and idade <= 59:
    print('Você é ADULTO')
else:
    print('Você é IDOSO!')
