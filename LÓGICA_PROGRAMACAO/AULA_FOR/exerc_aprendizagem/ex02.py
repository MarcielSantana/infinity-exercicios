# Exercicio 2 - Escreva um programa que peça ao usuário 5 números. Mostre a soma desses números.

soma = 0
for i in range(0, 5):
    num = int(input("digite um número: "))
    soma = soma + num
print(f"A soma dos números digitados é {soma}")
