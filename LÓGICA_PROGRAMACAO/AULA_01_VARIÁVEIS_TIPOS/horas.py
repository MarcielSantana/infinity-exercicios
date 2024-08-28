# EXERCICIO_19. Solicite somente as horas atuais para o usuário e verifique se o horário atual é antes das 12:00 ou depois das 18:00.
# Não utilize if.
hora = float(input('Que horas são agora? '))
am = 12;00
pm = 18;00
print(f'Agora são {hora}, {hora < am or hora > pm}')
