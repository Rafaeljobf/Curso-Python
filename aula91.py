import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__
lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)