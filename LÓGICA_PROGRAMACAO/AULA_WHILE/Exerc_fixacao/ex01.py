# Crie um programa que pergunte se a pessoa quer continuar no programa.
# Caso ela diga 'sim', pergunte novamente


sim = input('Você quer continuar? ')
nao = input('Você quer continuar? ')

while sim == 'sim':
    print(f'Você digitou {sim}')
    sim = input('Você quer continuar? ')
print('Programa encerrado')
