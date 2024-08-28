# Escreva um programa que verifica o número do mês digitado pelo usuário e
# imprime a estação do ano correspondente.

# OUTONO: De março a maio
# INVERNO: De junho a agosto
# PRIMAVERA: De setembro a novembro
# VERÃO: de dezembro a fevereiro

mes = int(input('Digite o número do mês e saiba qual estação estamos: '))
estacao = ''
if mes == 3 or mes == 4 or mes == 5:
    estacao = 'Estamos no OUTONO'
elif mes == 6 or mes == 7 or mes == 8:
    estacao = 'Estamos no INVERNO'
elif mes == 9 or mes == 10 or mes == 11:
    estacao = 'Estamos na PRIMAVERA'
elif mes == 12 or mes == 1 or mes == 2:
    estacao = 'Estamos no VERÃO'
else:
    print('Número inválido, tente novamente de 1 a 12')
print(estacao)
