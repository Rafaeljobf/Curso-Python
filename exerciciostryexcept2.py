horario = input('Digite que horas são em números inteiros: ')

try:
    horario_int = int(horario)
    if horario_int >= 0 and horario_int<= 11:
        print('Bom dia!')
    elif horario_int >= 12 and horario_int <= 17:
        print('Boa tarde!')
    elif horario_int >= 18 and horario_int < 24:
        print('Boa noite!')
    else:
        print('Você não digitou um horário válido')
except:
    print('Você não digitou um horário')