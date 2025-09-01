from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass
    
    def depositar(self, deposito: float) -> float:
        if not isinstance(deposito, (int, float)):
            raise TypeError('Você não digitou um valor depositável')
        self.saldo += deposito
        self.detalhes(f'(DEPÓSITO: R${deposito})')
        return self.saldo
    
    def detalhes(self, msg: str ='') -> None:
        print(f'O seu saldo é R${self.saldo:.2f}. {msg}')
        print('--')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia}, {self.numero_conta}, {self.saldo})'
        return f'{class_name} {attrs}'
    
class ContaCorrente(Conta):
    def __init__(
            self, agencia: int, numero_conta: int,
            saldo: float = 0, limite: float = 0
        ):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    def sacar(self, saque: float) -> float:
        valor_pos_saque = self.saldo - saque
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= saque
            self.detalhes(f'(SAQUE: {saque})')
            return self.saldo     
           
        print('Você não tem saldo suficiente!')
        print(f'Seu limite é {self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO: R${saque})')
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia}, {self.numero_conta}, {self.saldo}, {self.limite})'
        return f'{class_name} {attrs}'

    
class ContaPoupanca(Conta):
    def sacar(self, saque: float) -> float:
        valor_pos_saque = self.saldo - saque

        if valor_pos_saque >= 0:
            self.saldo -= saque
            self.detalhes(f'(SAQUE: {saque})')
            return self.saldo        
        print('Você não tem saldo suficiente!')
        self.detalhes(f'(SAQUE NEGADO: R${saque})')
        return self.saldo
    
if __name__ == '__main__':
    cc1 = ContaCorrente(111, 2)
    cc1.depositar(100)
    cc1.sacar(150)
    cp1 = ContaPoupanca(222, 3)
    cp1.depositar(50)
    cp1.sacar(150)