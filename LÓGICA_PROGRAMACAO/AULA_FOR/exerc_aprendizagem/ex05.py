# Escreva um programa que substitua todas as letras a, b e c de uma string por asteristicos(*)
palavra = 'banana'

string_substituida = ''
for caractere in palavra:
    if caractere in 'abc':
        string_substituida += '*'
    else:
        string_substituida += caractere
print(string_substituida)
