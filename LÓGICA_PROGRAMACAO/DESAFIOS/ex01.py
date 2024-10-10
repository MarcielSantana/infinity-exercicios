import random

num_aleatorio = random.randint(1, 20)

num_sugerido = int(input('Digite um número de 1 a 20: '))

while num_sugerido != num_aleatorio:
    print('FALHOU. Tente novamente')
    num_sugerido = int(input('Digite um número de 1 a 20: '))
if num_sugerido == num_aleatorio:
    print('PARABÉNS')
