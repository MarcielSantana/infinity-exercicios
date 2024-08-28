# EXERCICIO 01 - Escreva um programa que verifica se uma determinada palavra está presente em uma frase. 
# Se estiver, imprima a frase.
palavra = 'Python'
frase = 'Aprender Python está sendo muito legal.'

if palavra in frase:
    print(f'A palavra que você procura é {palavra}')
else:
    print('ERROR: Não há essa palavra na frase')
