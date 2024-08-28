
frase = input('Escreva uma palavra ou frase e veja quantas vogais ela tem: ')
vogais = 'aeiouAEIOU'
contador = 0
for vog in frase:
    if vog in vogais:
        contador += 1
print(f'A frase ou palavra tem {contador} vogais')
