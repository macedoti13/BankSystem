# Classes relacionadas aos tratamentos de exceção
class ErroNegativo(Exception):
    """ Classe para tratar saque/depositos com valores negativos """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Tentativa de Saque/Deposito com valor 0 ou negativo: {self.valor}R$.'



class ErroSaldo(Exception):
    """ Classe para tratar saldos com valores insuficientes """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Você não tem saldo suficiente para fazer saque de: {self.valor}R$.'



class NumeroInvalido(Exception):
    """ Classe para impedir a entrada de numeros de conta inválidos"""
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Numero Inválido: {self.valor}.'



class NomeInvalido(Exception):
    """ Classe para impedir a entrada de nomes inválidos"""
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Nome Inválido: {self.valor}.'



class CpfInvalido(Exception):
    """ Classe para impedir a entrada de cpfs inválidos """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'CPF Inválido: {self.valor}.'



class SaldoInvalido(Exception):
    """ Classe para impedir a entrada de um saldo inválido """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Saldo Inválido: {self.valor}R$.'



class LimiteInvalido(Exception):
    """ Classe para impedir a entrada de um limite inválido """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Limite Inválido: {self.valor}R$.'



class RiscoInvalido(Exception):
    """ Classe para impedir a entrada de um risco inválido """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Risco Inválido: {self.valor}.'



class RendimentoInvalido(Exception):
    """ Classe para impedir a entrada de um rendimento inválido """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Rendimento Inválido: {self.valor}%.'