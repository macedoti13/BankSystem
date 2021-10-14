class Moeda():
    """ Representa o tipo de moeda utilizada nos saques e depositos feitos pelas contas """

    def __init__(self, tipo='real', valor=0):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        print(f'Moeda: {self.tipo}')

    def __add__(self, quantidade):
        if isinstance(quantidade, int):
            novo_valor = self.valor + quantidade
        elif isinstance(quantidade, float):
            novo_valor = self.valor + quantidade
        else:
            novo_valor = self.valor + quantidade.valor
        return novo_valor

    def __sub__(self, quantidade):
        if isinstance(quantidade, int):
            novo_valor = self.valor - quantidade
        elif isinstance(quantidade, float):
            novo_valor = self.valor - quantidade
        else:
            novo_valor = self.valor - quantidade.valor
        return novo_valor

    def __mul__(self, quantidade):
        if isinstance(quantidade, int):
            novo_valor = self.valor * quantidade
        elif isinstance(quantidade, float):
            novo_valor = self.valor * quantidade
        else:
            novo_valor = self.valor * quantidade.valor
        return novo_valor

    def __pow__(self, quantidade):
        if isinstance(quantidade, int):
            novo_valor = self.valor ** quantidade
        elif issubclass(quantidade, float):
            novo_valor = self.valor ** quantidade
        else:
            novo_valor = self.valor ** quantidade.valor
        return novo_valor

    def __truediv__(self, quantidade):
        if isinstance(quantidade, int):
            novo_valor = self.valor / quantidade
        elif isinstance(self, float):
            novo_valor = self.valor / quantidade
        else:
            novo_valor = self.valor / quantidade.valor
        return novo_valor

    def __floordiv__(self, quantidade):
        if isinstance(quantidade, int):
            novo_valor = self.valor // quantidade
        elif isinstance(quantidade, float):
            novo_valor = self.valor // quantidade
        else:
            novo_valor = self.valor // quantidade.valor
        return novo_valor
    
    def __mod__(self, quantidade):
        if isinstance(quantidade, int):
            novo_valor = self.valor % quantidade
        elif isinstance(quantidade, float):
            novo_valor = self.valor % quantidade
        else:
            novo_valor = self.valor % quantidade.valor
        return novo_valor

    def __eq__(self, quantidade):
        if isinstance(quantidade, int):
            return self.valor == quantidade
        elif isinstance(quantidade, float):
            return self.valor == quantidade
        else:
            return self.valor == quantidade.valor

    def __ne__(self, quantidade):
        if isinstance(quantidade, int):
            return self.valor != quantidade
        elif isinstance(quantidade, float):
            return self.valor != quantidade
        else:
            return self.valor != quantidade.valor

    def __lt__(self, quantidade):
        if isinstance(quantidade, int):
            return self.valor < quantidade
        elif isinstance(quantidade, float):
            return self.valor < quantidade
        else:
            return self.valor < quantidade.valor

    def __le__(self, quantidade):
        if isinstance(quantidade, int):
            return self.valor <= quantidade
        elif isinstance(quantidade, float):
            return self.valor <= quantidade
        else:
            return self.valor <= quantidade.valor

    def __gt__(self, quantidade):
        if isinstance(quantidade, int):
            return self.valor > quantidade
        elif isinstance(quantidade, float):
            return self.valor > quantidade
        else:
            return self.valor > quantidade.valor

    def __ge__(self, quantidade):
        if isinstance(quantidade, int):
            return self.valor >= quantidade
        elif isinstance(quantidade, float):
            return self.valor >= quantidade
        else:
            return self.valor >= quantidade.valor
    
    def __iadd__(self, quantidade):
        if isinstance(quantidade, int):
            self.valor += quantidade
        elif isinstance(quantidade, float):
            self.valor += quantidade
        else:
            self.valor += quantidade.valor
        return self.valor

    def __isub__(self, quantidade):
        if isinstance(quantidade, int):
            self.valor -= quantidade
        elif isinstance(quantidade, float):
            self.valor -= quantidade
        else:
            self.valor -= quantidade.valor
        return self.valor

    def __imul__(self, quantidade):
        if isinstance(quantidade, int):
            self.valor *= quantidade
        elif isinstance(quantidade, float):
            self.valor *= quantidade
        else:
            self.valor *= quantidade.valor
        return self.valor

    def __ipow__(self, quantidade):
        if isinstance(quantidade, int):
            self.valor **= quantidade
        elif issubclass(quantidade, float):
            self.valor **= quantidade
        else:
            self.valor **= quantidade.valor
        return self.valor

    def __idiv__(self, quantidade):
        if isinstance(quantidade, int):
            self.valor /= quantidade
        elif isinstance(self, float):
            self.valor /= quantidade
        else:
            self.valor /= quantidade.valor
        return self.valor

    def __ifloordiv__(self, quantidade):
        if isinstance(quantidade, int):
            self.valor //= quantidade
        elif isinstance(quantidade, float):
            self.valor //= quantidade
        else:
            self.valor //= quantidade.valor
        return self.valor
    
    def __imod__(self, quantidade):
        if isinstance(quantidade, int):
            self.valor %= quantidade
        elif isinstance(quantidade, float):
            self.valor %= quantidade
        else:
            self.valor %= quantidade.valor
        return self.valor