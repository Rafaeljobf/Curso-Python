# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        if valor not in ['Vermelho', 'Azul', 'Preto']:
            raise ValueError
        self._cor = valor


caneta = Caneta('Azul')
print(caneta.cor)

try:
    caneta.cor = 'Rosa'
except ValueError:
    print('Um erro foi encontrado na atribuição de nova cor.')