"""
Formatação básica de strings
s - strings
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100, 1.f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:1>10}')
print(f'{variavel:0<10}')
print(f'{1000.323212311232332323232323:,.2f}')
print(f'O hexadecimal de 1500 é {1500:06X}')