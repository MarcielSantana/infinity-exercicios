# Exercicio 8 - Escreva um programa que verifica o número do dia da semana (1 a 7)
# digitado pelo usuário e imprime o nome do dia correspondente

numero_dia = int(input('Digite um número de 1 a 7 e veja que dia é hoje: '))
if numero_dia == 1:
    print('Hoje é DOMINGO')
elif numero_dia == 2:
    print('Hoje é SEGUNDA')
elif numero_dia == 3:
    print('Hoje é TERÇA')
elif numero_dia == 4:
    print('Hoje é QUARTA')
elif numero_dia == 5:
    print('Hoje é QUINTA')
elif numero_dia == 6:
    print('Hoje é SEXTA')
elif numero_dia == 7:
    print('Hoje é SÁBADO')
else:
    print('Número inválido! Digite um de 1 a 7')
