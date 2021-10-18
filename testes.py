from Contas import ContaBancaria as CB, ContaCorrente, ContaInvestimento, ContaPoupanca
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
    arq.write('sacar: contaPoupanca -> 909\n')
    arq.write('depositar: contaCorrente -> 20\n')
    arq.write('depositar: contaPoupanca -> 20\n')
    arq.write('depositar: contaInvestimento -> 20\n')
    arq.write('saldo: contaCorrente\n')
    arq.write('saldo: contaPoupanca\n')
    arq.write('saldo: contaInvestimento\n')
    arq.write('rendimento: contaCorrente -> 20 dias\n')
    arq.write('rendimento: contaPoupanca -> 20 dias\n')
    arq.write('rendimento: contaInvestimento -> 10 dias\n')



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

with open(nome_arq, 'r') as arq:
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
        
        