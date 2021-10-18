import sys
from Contas import ContaBancaria, ContaCorrente, ContaInvestimento, ContaPoupanca
import Contas as C
import Erros as E
import Moeda as M

def readfile(a):
    global tipo_conta
    if a.find('criar:') != -1:
        if a.find('contaInvestimento') != -1:
            tipo_conta = 'contaInvestimento'
        elif a.find('contaCorrente') != -1:
            tipo_conta = 'contaCorrente'
        elif a.find('contaPoupanca') != -1:
            tipo_conta = 'contaPoupanca'

    if a.find('saldoInicial:') != -1:
        global saldo
        saldo = a[14:]
        saldo = int(saldo)

    if a.find('id:') != -1: 
        global numero_conta
        numero_conta = a[4:]

    if a.find('limiteChequeEspecial:') != -1:
        global limite
        limite = a[22:]
        limite = int(limite)
        global contaC
        try:
            contaC = ContaCorrente(numero_conta, nome, cpf, saldo, limite)
        except E.NumeroInvalido as e:
            arql.write(str(e,'\n'))
        except E.NomeInvalido as e:
            arql.write(str(e,'\n'))
        except E.CpfInvalido as e:
            arql.write(str(e,'\n'))
        except E.LimiteInvalido as e:
            arql.write(str(e,'\n'))
        except E.SaldoInvalido as e:
            arql.write(str(e,'\n'))

    if a.find('taxaRendimento:') != -1:
        global rendimento
        rendimento = a[16:]
        rendimento = float(rendimento)
        global contaP
        try:
            contaP = ContaPoupanca(numero_conta, nome, cpf, saldo, rendimento)
        except E.NumeroInvalido as e:
            arql.write(str(e) + '\n')
        except E.NomeInvalido as e:
            arql.write(str(e) + '\n')
        except E.CpfInvalido as e:
            arql.write(str(e) + '\n')
        except E.RendimentoInvalido as e:
            arql.write(str(e) + '\n')
        except E.SaldoInvalido as e:
            arql.write(str(e) + '\n')

    if a.find('tipoRisco:') != -1:
        global risco
        risco = a[11:16]
        risco = risco.lower()
        global contaI
        try:
            contaI = ContaInvestimento(numero_conta, nome, cpf, saldo, risco)
        except E.NumeroInvalido as e:
            arql.write(str(e) + '\n')
        except E.NomeInvalido as e:
            arql.write(str(e) + '\n')
        except E.CpfInvalido as e:
            arql.write(str(e) + '\n')
        except E.RiscoInvalido as e:
            arql.write(str(e) + '\n')
        except E.SaldoInvalido as e:
            arql.write(str(e) + '\n')

    if a.find('sacar:') != -1:
        if a.find('contaInvestimento') != -1: 
            try:
                contaI.saque(int(a[28:]))
            except E.ErroSaldo as e:
                arql.write(str(e) + '\n')
            except E.ErroNegativo as e:
                arql.write(str(e) + '\n')
        elif a.find('contaCorrente') != -1:
            try:
                contaC.saque_verboso(contaC, int(a[24:]))
            except E.ErroSaldo as e:
                arql.write(str(e) + '\n')
            except E.ErroNegativo as e:
                arql.write(str(e) + '\n')
        elif a.find('contaPoupanca') != -1:
            try:
                contaP.saque(int(a[24:]))
            except E.ErroSaldo as e:
                arql.write(str(e) + '\n')
            except E.ErroNegativo as e:
                arql.write(str(e) + '\n')

    if a.find('depositar:') != -1: 
        if a.find('contaInvestimento') != -1:
            try:
                contaI.deposito(int(a[32:]))
            except E.ErroNegativo as e:
                arql.write(str(e) + '\n')
        elif a.find('contaCorrente') != -1:
            try:
                contaC.deposito(int(a[28:]))
            except E.ErroNegativo as e:
                arql.write(str(e) + '\n')
        elif a.find('contaPoupanca') != -1:
            try:
                contaP.deposito(int(a[28:]))
            except E.ErroNegativo as e:
                arql.write(str(e) + '\n')

    if a.find('saldo:') != -1:
        if a.find('contaInvestimento') != -1:
            contaI.checa_saldo()
        elif a.find('contaCorrente') != -1:
            contaC.checa_saldo()
        elif a.find('contaPoupanca') != -1:
            contaP.checa_saldo()

    if a.find('rendimento:') != -1:
        if a.find('contaInvestimento') != -1:
            try:
                contaI.checa_rendimento(int(a[33:35]))
            except E.ErroNegativo as e:
                arql.write(str(e) + '\n')
        elif a.find('contaCorrente') != -1:
            try:
                contaC.checa_rendimento(int(a[29:31]))
            except E.ErroNegativo as e:
                arql.write(str(e) + '\n')
        elif a.find('contaPoupanca') != -1: 
            try:
                contaP.checa_rendimento(int(a[29:31]))
            except E.ErroNegativo as e:
                arql.write(str(e) + '\n')

for arg in sys.argv:
    with open(arg, 'r') as arq:
        i=1
        nome = arq.readline()
        cpf = arq.readline()
        cpf = cpf[5:16]
        cpf = str(cpf)
        tipo_conta = ''
        arql = open(f'{i}.log','w')
    
        for line in arq:
            a = line
            readfile(a)
        arql.close()
    
        with open(f'{i}.saida','w') as arqs:
            arqs.write(f'Saldo da conta Corrente: {str(contaC.checa_saldo())} \n')
            arqs.write(f'Saldo da conta Poupanca: {str(contaP.checa_saldo())} \n')
            arqs.write(f'Saldo da conta Investimento: {str(contaI.checa_saldo())} \n')
            arqs.write(f'Rendimento de 30 dias da conta corrente: {str(contaC.checa_rendimento(30))} \n')
            arqs.write(f'Rendimento de 30 dias da conta Poupanca: {str(contaP.checa_rendimento(30))} \n')
            arqs.write(f'Rendimento de 30 dias da conta Investimento: {str(contaI.checa_rendimento(30))} \n')

        i+=1

"""
contaInvest = C.ContaInvestimento('0001', 'Thiago de Almeida Macedo', '05343493878', 1000, 'alto')
contaCorr = C.ContaCorrente('0002', 'Antonio Macedo', '34559303452', 10000, -500)
contaPoup = C.ContaPoupanca('0003', 'Simone de Almeida', '38475937495', 3000, 0.5)
print()
print('testando conta investimento')
print()
print(contaInvest)
print(f'numero contaInvest: {contaInvest.numero_conta},  Nome do cliente: {contaInvest.nome_cliente}, cpf do cliente: {contaInvest.cpf}, \
saldo: {contaInvest.saldo}, risco: {contaInvest.risco}')
contaInvest.deposito(100)
print(contaInvest.checa_rendimento(30))
print(contaInvest.checa_saldo())
contaInvest.saque(400)
print(contaInvest.checa_saldo())
contaInvest.testeDeAtributoDesconhecido
print(contaInvest.testeDeMetodoDesconhecido())
print()
print('Testando conta corrente')
print()
print(contaCorr)
print(f'numero contaCorr: {contaCorr.numero_conta}, nome do cliente: {contaCorr.nome_cliente}, cpf da conta: {contaCorr.cpf}, \
saldo: {contaCorr.saldo}, limite: {contaCorr.limite}')
print(contaCorr.checa_saldo())
contaCorr.deposito(1000)
print(contaCorr.checa_saldo())
print(contaCorr.checa_rendimento(30))
contaCorr.saque(1000)
print(contaCorr.checa_saldo())
contaCorr.testeDeAtributoDesconhecido
print(contaCorr.testeDeMetodoDesconhecido())
print()
print('Testando conta poupança')
print()
print(contaPoup)
print(f'numero contaPoup: {contaPoup.numero_conta}, nome do cliente: {contaPoup.nome_cliente}, cpf da conta: {contaPoup.cpf}, \
saldo: {contaPoup.saldo}, limite: {contaPoup.limite}')
print(contaPoup.checa_saldo())
contaPoup.deposito(1000)
print(contaPoup.checa_saldo())
print(contaPoup.checa_rendimento(30))
contaPoup.saque(1000)
print(contaPoup.checa_saldo())
contaPoup.testeDeAtributoDesconhecido
print(contaPoup.testeDeMetodoDesconhecido())
print()
print('Testando contador de contas')
print()
ContaBancaria.quantidade_contas()
ContaCorrente.qtd_contas_corrente()
ContaInvestimento.qtd_contas_investimento()
ContaPoupanca.qtd_contas_poupanca()
print()
print('Testando saque verboso')
print()
ContaBancaria.saque_verboso(contaCorr, 100)
print()
ContaBancaria.saque_verboso(contaInvest, 100)
print()
ContaBancaria.saque_verboso(contaPoup, 100)
print()
print('Testando criação de contas invalidas')
print()
try:
    print('conta corrente')
    print('testando nr invalido')
    contaA = ContaCorrente('-1234', 'joão felix', '34567834569', 9000, -0.5)
    print('testando nome invalido')
    contaB = ContaCorrente('0004', 'testecommaisde50letrasparadarerrodenomeeverseestafuncionando', '12345678912', 8000, -0.5)
    print('testando cpf invalido')
    contaC = ContaCorrente('0005', 'vitor pires', '12345', 7000, -0.8)
    print('testando saldo invalido')
    contaD = ContaCorrente('0006', 'joão terra', '12345678934', -500, -0.8)
    print('testando limite invalido')
    contaE = ContaCorrente('0006', 'augusto', '98765432123', 300, 13)
except E.NumeroInvalido as e:
    print(e)
except E.NomeInvalido as e:
    print(e)
except E.CpfInvalido as e:
    print(e)
except E.SaldoInvalido as e:
    print(e)
except E.LimiteInvalido as e:
    print(e)
except E.ErroSaldo as e:
    print(e)
print()
print('testando operações invalidas')
try:
    contaCorr.saque(100000)
except E.ErroSaldo as e:
    print(e)
try:
    contaCorr.saque(-100)
except E.ErroNegativo as e:
    print(e)
try:
    contaCorr.deposito(-1)
except E.ErroNegativo as e:
    print(e)
"""