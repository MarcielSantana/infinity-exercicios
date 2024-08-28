# Exercicio 4 - Escreva um que verifica se a idade digitada pelo usuário indica que ele 
# deve votar (idade >= 18 anos) ou não, e imprime uma mensagem correspondente.

idade = int(input('Qual sua idade? '))

if idade >= 18 and idade <= 69:
    print('Você já pode e deve votar')
elif idade >= 16 and 17 or idade > 70:
    print('Seu voto é importante, mas é FACULTATIVO')
else:
    print('Você ainda não pode votar. Aguarde mais um pouco!')
