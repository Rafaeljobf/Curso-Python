# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma class pode gerar várias instâncias
# Na classe o self é a própria instância

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0
    
    def __str__(self):
        return f'Carro: {self.marca} {self.modelo} na cor {self.cor}. (Velocidade atual: {self.velocidade})'

    def acelerar(self, valor):
        print(f'{self.modelo} está acelerando!')
        self.velocidade += valor
        print(f'A velocidade de {self.modelo} agora é de {self.velocidade}')

carro_fef = Carro('Chevrolet', 'Camaro', 'Rosa')
carro_fofilho = Carro('Lamborghni', 'Huracán', 'Roxo')

print(carro_fef)
print(carro_fofilho)

print()
carro_fef.acelerar(180)
print()
carro_fofilho.acelerar(220)