from Contas import ContaBancaria, ContaCorrente, ContaInvestimento, ContaPoupanca
import Contas as C
import Erros as E
import Moeda as M

nome_arq='teste.txt'
with open(nome_arq, 'w') as arq:
    arq.write('Dalvan Griebler\n')
    arq.write('CPF: 13318822008\n')
    arq.write('criar: contaCorrente\n')
    arq.write('saldoInicial: 400\n')
    arq.write('id: 1001\n')
    arq.write('limiteChequeEspecial: -100\n')
    arq.write('criar: contaPoupanca\n')
    arq.write('saldoInicial: 500\n')
    arq.write('id: 4001\n')
    arq.write('taxaRendimento: 0.5\n')
    arq.write('criar: contaInvestimento\n')
    arq.write('saldoInicial: 800\n')
    arq.write('id: 8001\n')
    arq.write('tipoRisco: Baixo\n')
    arq.write('sacar: contaInvestimento -> 20\n')
    arq.write('sacar: contaCorrente -> 420\n')
    arq.write('depositar: contaCorrente -> 20\n')
    arq.write('saldo: contaCorrente\n')
    arq.write('saldo: contaPoupanca\n')
    arq.write('saldo: contaInvestimento\n')
    arq.write('rendimento: contaCorrente -> 20 dias\n')
    arq.write('rendimento: contaPoupanca -> 20 dias\n')
    arq.write('rendimento: contaInvestimento -> 10 dias\n')



def readfile(a):
    if a.find('criar:') != -1:
        if a.find('contaInvestimento') != -1:
            tipo = 'contaInvestimento'
        elif a.find('contaCorrente') != -1:
            tipo = 'contaCorrente'
        elif a.find('contaPoupanca') != -1:
            tipo = 'contaPoupanca'

    if a.find('saldoInicial:') != -1:
        global saldo
        saldo = a[14:]
        print('saldo: ' + saldo)
        saldo = int(saldo)

    if a.find('id:') != -1:
        global id 
        id = a[4:]
        print('numero conta: ' + id)

    if a.find('limiteChequeEspecial::') != -1:
        global limite
        limite = a[22:]
        print('limite: ' + limite)
        limite = int(limite)

    if a.find('taxaRendimento:') != -1:
        global rendimento
        rendimento = a[16:]
        print('rendimento: ' + rendimento)
        rendimento = float(rendimento)

    if a.find('tipoRisco:') != -1:
        global risco
        risco = a[11:]
        print('risco:' + risco)

    if a.find('sacar:') != -1:
        if a.find('contaInvestimento') != -1: 
            print('saque na conta investimento')
        elif a.find('contaCorrente') != -1:
            print('Saque na conta corrente') ########
        elif a.find('contaPoupanca') != -1:
            print('saque na conta poupanca') ##########

    if a.find('depositar:') != -1: 
        if a.find('contaInvestimento') != -1:
            print('deposito na conta investimento') ########
        elif a.find('contaCorrente') != -1:
            print('deposito na conta corrente') ########
        elif a.find('contaPoupanca') != -1:
            print('deposito na conta poupanca') ###########

    if a.find('saldo:') != -1:
        if a.find('contaInvestimento') != -1:
            print('saldo da conta investimento') #########
        elif a.find('contaCorrente') != -1:
            print('saldo da conta corrente') ##########
        elif a.find('contaPoupanca') != -1:
            print('saldo da conta poupanca') ###########

    if a.find('rendimento:') != -1:
        if a.find('contaInvestimento') != -1:
            print('rendimento da conta investimento') #######
        elif a.find('contaCorrente') != -1:
            print('rendimento da conta corrente') ########
        elif a.find('contaPoupanca') != -1: 
            print('rendimento da conta poupanca') ######



with open(nome_arq, 'r') as arq:
    nome = arq.readline()
    cpf = arq.readline()
    cpf = cpf[5:]
    print(f'nome = {nome}', end='')
    print(f'cpf = {cpf}', end='')
    for line in arq:
        a = line
        print(a, end='')