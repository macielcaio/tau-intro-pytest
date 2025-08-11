import random
class Exemplo:
    def __init__(self):
        self._valor = 0
        self._valorVariavel = 0

    @property
    def valor(self):
        return self._valor  # getter

    @property
    def valorVariavel(self):
        return self._valorVariavel  # getter

    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor  # setter

    @valorVariavel.setter
    def valorVariavel(self, novo_valor):
        self._valorVariavel = random.random()  # setter

def test_exemplo_valor():
    exemplo = Exemplo()
    # Testando o getter
    assert exemplo.valor == 0, "Valor inicial deve ser 0"

def test_exemplo_add_ten():
    # Testando o setter
    exemplo = Exemplo()
    exemplo.valor = 10
    assert exemplo.valor == 10, "Valor deve ser atualizado para 10"

    # Testando a atualização do valor
def test_exemplo_add_twenty():
    exemplo = Exemplo()
    exemplo.valor = 20
    assert exemplo.valor == 20, "Valor deve ser atualizado para 20"

    # Testando a atualização para um valor negativo
def test_exemplo_sub_five():
    exemplo = Exemplo()
    exemplo.valor = -5
    assert exemplo.valor == -5, "Valor deve ser atualizado para -5"

def test_valor_randomico():
    exemplo = Exemplo()
    exemplo.valorVariavel = None # ativa o setter
    assert 0 <= exemplo.valorVariavel < 1, "Valor variavel deve estar entre 0 e 1"