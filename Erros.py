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
        return f'Voce nao tem saldo suficiente para fazer saque de: {self.valor}R$.'



class NumeroInvalido(Exception):
    """ Classe para impedir a entrada de numeros de conta invalidos"""
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Numero Invalido: {self.valor}.'



class NomeInvalido(Exception):
    """ Classe para impedir a entrada de nomes invalidos"""
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Nome Invalido: {self.valor}.'



class CpfInvalido(Exception):
    """ Classe para impedir a entrada de cpfs invalidos """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'CPF Invalido: {self.valor}.'



class SaldoInvalido(Exception):
    """ Classe para impedir a entrada de um saldo invalido """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Saldo Invalido: {self.valor}R$.'



class LimiteInvalido(Exception):
    """ Classe para impedir a entrada de um limite invalido """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Limite Invalido: {self.valor}R$.'



class RiscoInvalido(Exception):
    """ Classe para impedir a entrada de um risco invalido """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Risco Invalido: {self.valor}.'



class RendimentoInvalido(Exception):
    """ Classe para impedir a entrada de um rendimento invalido """
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'Rendimento Invalido: {self.valor}%.'