"""
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Loop infinito até senha ser digitada corretamente')"
"""
texto = 'Python'

novo_texto = ''
for letra in texto:
    print(letra)
    novo_texto += f'*{letra}'
print(novo_texto + '*')


