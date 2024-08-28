# Exercicio 3 - Faça um programa que leia um nome de usuário e a sua senha e
# não aceite a senha igual ao nome de usuário, mostrando uma mensagem de erro e
# voltando a pedir as informações.

usuario = input('Digite seu usuário ')
senha = input('Digite sua senha ')

while usuario == senha:
    print('Usuário e senha NÃO podem ser iguais. Tente novamente')
    usuario = input('Digite seu usuário ')
    senha = input('Digite sua senha ')
print('Cadastro realizado com sucesso!')
