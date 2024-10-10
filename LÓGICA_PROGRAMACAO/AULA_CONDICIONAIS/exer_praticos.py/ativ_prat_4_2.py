# ATIVIDADE PRÁTICA 4
# EXERCICIO 2 - imprimir a nota e se a pessoa está aprovada ou não!
num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))

media = (num1 + num2) / 2

print(f'A MÉDIA de {num1} e {num2} é {media}')
resultado = ''
if media >= 7:
    resultado = 'Parabéns! Você foi APROVADO'
elif media == 10:
    resultado = 'Parabéns! APROVADO COM DISTINÇÃO'
else:
    resultado = 'Infelizmente você está REPROVADO'

print(resultado)
