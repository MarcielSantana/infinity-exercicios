# SOLUÇÃO 1:
numeros = []

for i in range(5):
    num = int(input('Digite um número '))
    numeros.append(num)

print(numeros)

# SOLUÇÃO 2:

numeros = []
contador = 0

while contador < 5:
    num = int(input('Digite um número '))
    numeros.append(num)
    contador += 1

print(numeros)
