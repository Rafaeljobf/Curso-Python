# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2025  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('Rafael', 20)
p2 = Pessoa.criar_com_50_anos('Gabriel')
print(vars(p1))
print(vars(p2))

p3 = Pessoa.criar_sem_nome(22)
print(vars(p3))
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()