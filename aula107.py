# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(step= 8, start= 16)
r1 = range(16, 100, 8)

print('c1', hasattr(c1, '__iter__'))

for i in c1:
    print(i)
    if i >= 100:
        break
print()
print('range:')

for i in r1:
    print(i)