class Animal:

    def __init__(self, nome):
        self.nome = nome

    def comer(self, alimento):
        self.alimento = alimento
        return f'{self.nome} está comendo {self.alimento}'
    
leao = Animal('Leão')
print(leao.nome)
print(leao.comer('carne'))
print(leao.comer('baião'))
