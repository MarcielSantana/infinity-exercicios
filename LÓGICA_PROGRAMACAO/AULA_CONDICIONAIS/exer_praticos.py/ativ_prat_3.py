# ATIVIDADE PRÁTICA 3
# letra = input('Digite F ou M para verificar o sexo da pessoa ').upper() -
# pode usar o método "upper()" para transformar a letra digitada em maisculo
# caso o usuário escreva assim

letra = input('Digite F ou M para verificar o sexo da pessoa ')
if letra == 'F' or letra == 'f':
    print('O sexo é Feminino')
elif letra == 'M' or letra == 'm':
    print('O sexo é Masculino')
else:
    print('sexo não existe')
