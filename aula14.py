a = 'A'
b = 'B'
c = '1.1'
d = 'brother'
string = 'a = {nome1}, b = {nome2}, c = {nome3} d = {nome4}'
formato = string.format(
    nome1=a, nome2=b, nome3=c, nome4=d)

print(formato)