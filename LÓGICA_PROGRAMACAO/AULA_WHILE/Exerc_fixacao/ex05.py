# EXERCICIO 5 - Solicite que o usuário digite números inteiros positivos 
# e exiba a soma desses números. Encerre o programa quando o usuário digitar
# um número negativo

num = int(input('Digite um número positivo (digite um negativo para encerrar):  '))
soma = 0
while num > 0:
    soma += num
    print(soma)
    num = int(input('Digite um número positivo (digite um negativo para encerrar):  '))
print('Programa encerrado')