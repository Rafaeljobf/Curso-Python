import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, name: str):
        self._nome = name

    @property
    def idade(self) -> int:
        return self._idade
    
    @idade.setter
    def idade(self, age: int):
        self._idade = age

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome}, {self.idade})'
        return f'{class_name} {attrs}'
    
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None

if __name__ == '__main__':
    c1 = Cliente('Rafael', 20)
    c1.conta = contas.ContaCorrente(1, 2, 100, 100)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Fernanda', 19)
    c2.conta = contas.ContaPoupanca(2, 3, 500)
    print(c2)
    print(c2.conta)