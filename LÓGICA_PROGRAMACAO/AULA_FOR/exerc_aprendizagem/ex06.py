# Escreva um programa que receba uma frase (string) e imprima cada palavra em uma linha separada.
# A frase deverá acabar em . (ponto), ? ou !

frase = 'Python é uma linguagem poderosa'
palavra = ''
for caractere in frase:
    if caractere in '.?!':
        print(palavra)
        palavra = ''
    else:
        palavra += caractere
