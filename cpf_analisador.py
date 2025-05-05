
soma_total_1 = 0
soma_total_2 = 0
multiplicador = 10

while True:
    cpf = input('Digite o CPF: ')
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if not cpf.isdigit():
        print('CPF inválido')
        continue
    else:
        break

# PRIMEIRO DIGITO
for numero in cpf:
    soma_total_1 += int(numero) * multiplicador
    multiplicador -= 1
    if multiplicador == 1:
        break

# SEGUNDO DIGITO
multiplicador = 11
for numero in cpf:
    soma_total_2 += int(numero) * multiplicador
    multiplicador -= 1
    if multiplicador == 1:
        break


primeiro_digito = (soma_total_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

segundo_digito = (soma_total_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print('O primeiro dígito é:', primeiro_digito)
print('O segundo dígito é:', segundo_digito)


    
