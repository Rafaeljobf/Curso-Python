import contas
import pessoa

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoa.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_conta', False)
        return False
    
    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False
    
    def checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('checa_se_conta_e_do_cliente', False)
        return False
    

    def autenticar(self, cliente: pessoa.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self.checa_se_conta_e_do_cliente(cliente, conta)
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias}, {self.clientes}, {self.contas})'
        return f'{class_name} {attrs}'

if __name__ == '__main__':
    c1 = pessoa.Cliente('Rafael', 20)
    cc1 = contas.ContaCorrente(111, 2, 100, 100)
    c1.conta = cc1
    c2 = pessoa.Cliente('Fernanda', 19)
    cp1 = contas.ContaPoupanca(222, 3, 500)
    c2.conta = cp1
    banco = Banco()

    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        cc1.sacar(50)
    
    
   