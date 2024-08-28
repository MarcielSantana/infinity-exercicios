# Exercicio 1 - Faça um programa que calcule e mostre a média artimética de três notas.

soma = 0
for index in range(0, 3):
    nota = float(input("digite a nota: "))
    soma = soma + nota
    media = soma / 3
    print(media)
