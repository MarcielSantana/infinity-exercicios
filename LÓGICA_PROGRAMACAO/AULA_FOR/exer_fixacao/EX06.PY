# Exercicio 6 - Escreva um programa que conte quantas vezes um determinado
# caractere aparece na frase
frase = input('Digite uma frase ')
letra = input('Digite qual letra quer contar: ')
caractere = frase.count(letra)
print(f'A letra "{letra}" aparece {caractere} vez(es)')


# OUTRA SOLUÇÃO:
frase = input('Digite uma frase ')
letra = input('Digite qual letra quer contar: ')
contador = 0
for caractere in frase:
    if caractere == letra:
        contador += 1
print(f'A letra "{letra}" aparece {contador} vez(es)')
