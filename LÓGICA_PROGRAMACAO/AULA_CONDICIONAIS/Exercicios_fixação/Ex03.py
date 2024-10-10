# EXERCICIO 03 - Escreva um programa que verifica se um usuário digitou corretamente o nome de usuário 
# "Admin" e senha "1234". Se ele digitou, mostre "Login realizado com sucesso!". 
# Se não, mostre "Nome de usuário ou senha incorretos".

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

user_padrao = 'admin'
senha_padrao = '1234'

if usuario == user_padrao and senha == senha_padrao:
    print('Login realizado com sucesso!')
else:
    print('Nome de usuário ou senha incorretos')
