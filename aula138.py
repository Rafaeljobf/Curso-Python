# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return f'{self.nome}'

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._fabricante = None
        self._motor = None

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    def __str__(self):
        return f'Carro: {self.nome} // Motor: {self._motor} // Fabricante: {self._fabricante}'

class Motor:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return f'{self.nome}'


fusca = Carro('Fusca')
v8 = Motor('V8')
volkswagen = Fabricante('Volkswagen')

fusca.fabricante = volkswagen
fusca.motor = v8

print(fusca)

ferrari = Carro('Ferrari')
ferrari.fabricante = volkswagen
ferrari.motor = v8

print(ferrari)