# EXERCICIO_20. Verifique se um número é positivo ou está entre 20 e 30.
num1 = int(input('Digite um número inteiro qualquer '))
positivo = num1 > 0
print(positivo or num1 >= 20 and num1 <= 30)
