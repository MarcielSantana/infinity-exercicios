# Exercicio 7 - Escreva um programa que encontre e imprima a primeira consoante
# em uma palavra fornecida pelo usuário. Utilize um loop for e a instrução break
# para interromper o loop assim que encontrar a primeira consoante.

palavra = input('Digite uma palavra: ')
vogais = 'aeiouAEIOU'
for letra in palavra:
    if letra not in vogais:
        print(f'A primeira consoante encontrada é "{letra}"')
        break
    else:
        print('ERROR: Não existe consoante nessa palavra')
