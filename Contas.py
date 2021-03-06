from abc import ABCMeta, abstractmethod
from Banco import Erros as E
from Banco import Moeda as M

# Classes relacionadas às contas bancarias
class ContaBancaria(metaclass=ABCMeta):
    """Classe da conta bancaria padrão. Possui diversos metodos padrão para todas as suas subclasses.

    Args:
        metaclass (ABCMeta, optional): Classe abstrata. Defaults to ABCMeta.

    Raises:
        E.NumeroInvalido: Tratamento de excessão caso o numero da conta seja invalido.
        E.NomeInvalido: Tratamento de excessão caso o nome do cliente seja invalido.
        E.CpfInvalido: Tratamento de excessão caso o cpf do cliente seja invalido.
        E.SaldoInvalido: Tratamento de excessão caso o saldo da conta seja invalido.
        E.ErroNegativo: Tratamento de excessão caso o valor do saque ou deposito seja negativo.
        E.ErroSaldo: Tratamento de excessão caso o cliente tente fazer um saque sem ter saldo suficiente.

    Returns:
        Objeto: Uma conta bancaria basica, com numero da conta, nome do cliente, cpf e saldo. Essa conta é capaz
        de realizar saques, depositos e consultar seus dados.
    """
    contas = 0
    rendimento = 0

    def __init__(self, numero_conta, nome_cliente, cpf, saldo):
        """Função de criação do objeto ContaBancaria.

        Args:
            numero_conta (str): Numero da conta do cliente.
            nome_cliente (str): Nome completo do cliente.
            cpf (str): CPF do cliente.
            saldo (float): Saldo inicial da conta.

        Raises:
            E.NumeroInvalido: Excessão caso o numero da conta não esteja dentro do padrão.
            E.NomeInvalido: Excessão caso o nome do cliente não enteja dentro do padrão.
            E.CpfInvalido: Excessão caso o CPF não esteja dentro do padrão.
            E.SaldoInvalido: Excessão caso o saldo da conta não enteja dentro do padrão.
        """
        if 0 > int(numero_conta) or 9999 < int(numero_conta):
            raise E.NumeroInvalido(numero_conta)
        else:
            self.__numero_conta = numero_conta
        
        if len(str(nome_cliente)) > 50:
            raise E.NomeInvalido(nome_cliente)
        else:
            self.__nome_cliente = nome_cliente

        if len(str(cpf)) != 11:
            raise E.CpfInvalido(cpf)
        else:
            self.__cpf = cpf

        if float(saldo) < 0.0:
            raise E.SaldoInvalido(saldo)
        else:
            self.__saldo = saldo

        ContaBancaria.add_conta()
        
    # Getter do atributo numero_conta    
    @property
    def numero_conta(self):
        return self.__numero_conta

    # Getter do atributo nome_cliente
    @property
    def nome_cliente(self):
        return self.__nome_cliente

    # Getter do atributo cpf
    @property
    def cpf(self):
        return self.__cpf

    # Getter do atributo saldo
    @property
    def saldo(self):
        return self.__saldo

    # Setter do atributo saldo
    @saldo.setter
    def saldo(self, novo_saldo):
        if isinstance(novo_saldo, int):
            self.__saldo = novo_saldo
        elif isinstance(novo_saldo, float):
            self.__saldo = novo_saldo


    def deposito(self, quantidade):
        """Realiza um deposito (aumenta o valor do saldo) na conta.

        Args:
            quantidade (float): Valor a ser adicionado no saldo da conta.

        Raises:
            E.ErroNegativo: Excessão caso o valor do deposito seja negativo.
        """
        if quantidade <= 0:
            raise E.ErroNegativo(quantidade)
        else:
            self.saldo += quantidade
            print(f'Deposito de {quantidade}R$ realizado.')


    def saque(self, quantidade):
        """Realiza um saque (diminui o valor do saldo) na conta.

        Args:
            quantidade (float): Valor a ser retirado do saldo da conta.

        Raises:
            E.ErroNegativo: Excessão caso o valor do saque seja negativo.
            E.ErroSaldo: Excessão caso o valor do saque seja maior que o saldo da conta.
        """
        if quantidade <= 0:
            raise E.ErroNegativo(quantidade)
        elif quantidade > self.saldo:
            raise E.ErroSaldo(quantidade)
        else:
            self.saldo -= quantidade
            print(f'Saque realizado no valor de {quantidade}R$')
    

    def checa_saldo(self):
        """Consulta o saldo da conta.

        Returns:
            str: texto formatado que contem o saldo atual da conta.
        """
        return f'O saldo da conta e de: {self.saldo}R$'

    # Função para consultar o rendimento
    @abstractmethod
    def checa_rendimento(self, dias):
        pass 

    # Função para tratar acesso a atributos desconhecidos
    def __getattr__(self, nome):
        print('Atributo/Metodo desconhecido:', nome)
        return self.metodo_desconhecido

    # Função para metodos desconhecidos
    def metodo_desconhecido(self):
        return -1

    # Função para mostrar a quantidade de contas criadas ao todo
    @staticmethod
    def quantidade_contas():
        print(f'Quantidade total de contas criadas: {ContaBancaria.contas}.')

    # Função para mostrar na tela uma mensagem quando uma conta é criada
    @staticmethod
    def nova_conta(nome_cliente):
        print(f'Uma nova conta bancaria foi criada em nome de {nome_cliente}.')

    # Função para adcionar uma nova conta ao contador de contas
    @classmethod
    def add_conta(cls):
        cls.contas += 1

    # Função para mostrar a quantidade de contas criadas ao todo e a quantidade de cada tipo de conta
    @staticmethod
    def status_conta():
        ContaCorrente.qtd_contas_corrente()
        ContaInvestimento.qtd_contas_investimento()
        ContaPoupanca.qtd_contas_poupanca()
        ContaBancaria.quantidade_contas()

    @staticmethod
    def mostra_dados_basicos(obj):
        print(f'Numero da conta: {obj.numero_conta}')
        print(f'Nome do cliente: {obj.nome_cliente}')
        print(f'CPF do cliente: {obj.cpf}')
        print(f'Saldo da conta: {obj.saldo}')

    @staticmethod
    def saque_verboso(obj, valor):
        ContaBancaria.mostra_dados_basicos(obj)
        if obj == ContaCorrente:
            print(f'Limite da conta: {obj.limite}')
        elif obj == ContaInvestimento:
            print(f'Risco associado: {obj.rico}')
        elif obj == ContaPoupanca:
            print(f'Rendimento da conta: {obj.rendimento}')
        obj.saque(valor)
        print(obj.checa_saldo())
        




class ContaCorrente(ContaBancaria):
    """ Subclasse Conta Corrente"""
    rendimento = 0.01
    contasCorrente = 0

    def __init__(self, numero_conta, nome_cliente, cpf, saldo, limite):
        super().__init__(numero_conta, nome_cliente, cpf, saldo)
        if limite > 0:
            raise E.LimiteInvalido(limite)
        else:
            self.__limite = limite

        ContaCorrente.nova_conta(self.nome_cliente)
        ContaCorrente.add_conta_corrente()

    # Getter do atributo limite
    @property
    def limite(self):
        return self.__limite

    def __str__(self):
        return f'Conta Corrente em nome de {self.nome_cliente}.'

    @staticmethod
    def qtd_contas_corrente():
        print(f'Quantidade de contas corrente criadas: {ContaCorrente.contasCorrente}.')
    
    @staticmethod
    def nova_conta(nome_cliente):
        print(f'Uma nova conta corrente foi criada em nome de {nome_cliente}.')

    @classmethod
    def add_conta_corrente(cls):
        cls.contasCorrente += 1

    def checa_rendimento(self, dias):
        a = (self.saldo * self.rendimento) * (dias/30)
        return f'O rendimento de seu saldo nos proximos {dias} dias e de: {a}R$'






class ContaInvestimento(ContaBancaria):
    """ Subclasse Conta Investimento """
    rendimento = 0
    contasInvestimento = 0

    def __init__(self, numero_conta, nome_cliente, cpf, saldo, risco):
        super().__init__(numero_conta, nome_cliente, cpf, saldo)
        if str(risco).lower() != 'alto' and str(risco).lower() != 'medio' and str(risco).lower() != 'baixo':
            raise E.RiscoInvalido(risco)
        else:
            self.__risco = risco
        
        ContaInvestimento.nova_conta(self.nome_cliente)
        ContaInvestimento.add_conta_investimento()
        ContaInvestimento.calcula_rendimento(self)

    # Função que calcula o investimento de acordo com risco 
    def calcula_rendimento(self):
        if self.__risco == 'alto':
            self.rendimento = 0.5
        elif self.__risco == 'medio':
            self.rendimento = 0.25
        else:
            self.rendimento = 0.1
             
    # Getter do atributo risco
    @property
    def risco(self):
        return self.__risco

    def __str__(self):
        return f'Conta investimento em nome de {self.nome_cliente}.'

    @staticmethod
    def qtd_contas_investimento():
        print(f'Quantidade de contas investimento criadas: {ContaInvestimento.contasInvestimento}.')

    @staticmethod
    def nova_conta(nome_cliente):
        print(f'Uma nova conta investimento foi criada em nome de {nome_cliente}.')

    @classmethod
    def add_conta_investimento(cls):
        cls.contasInvestimento += 1

    def checa_rendimento(self, dias):
        a = (self.saldo * self.rendimento) * (dias/30)
        return f'O rendimento de seu saldo nos proximos {dias} dias e de: {a}R$'






class ContaPoupanca(ContaBancaria):
    """ Subclasse Conta Poupanca """
    contasPoupanca = 0

    def __init__(self, numero_conta, nome_cliente, cpf, saldo, rendimento):
        super().__init__(numero_conta, nome_cliente, cpf, saldo)
        if 0 > float(rendimento) or 1 < float(rendimento):
            raise E.RendimentoInvalido(rendimento)
        else:
            self.__rendimento = rendimento

        ContaPoupanca.nova_conta(self.nome_cliente)
        ContaPoupanca.add_conta_poupanca()
        

    # Getter do atributo rendimento
    @property
    def rendimento(self):
        return self.__rendimento

    def __str__(self):
        return f'Conta poupança em nome de {self.nome_cliente}.'

    @staticmethod
    def qtd_contas_poupanca():
        print(f'Quantidade de contas poupança criadas: {ContaPoupanca.contasPoupanca}.')

    @staticmethod
    def nova_conta(nome_cliente):
        print(f'Uma nova conta poupanca foi criada em nome de {nome_cliente}.')

    @classmethod
    def add_conta_poupanca(cls):
        cls.contasPoupanca += 1

    def checa_rendimento(self, dias):
        a = (self.saldo * self.rendimento) * (dias/30)
        return f'O rendimento de seu saldo nos proximos {dias} dias eh de: {a}R$'