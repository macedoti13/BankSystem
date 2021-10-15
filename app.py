from Contas import ContaBancaria, ContaCorrente, ContaInvestimento, ContaPoupanca
import Contas as C
import Erros as E
import Moeda as M

contaInvest = C.ContaInvestimento('0001', 'Thiago de Almeida Macedo', '05343493878', 1000, 'alto')
contaCorr = C.ContaCorrente('0002', 'Antonio Macedo', '34559303452', 10000, -500)
contaPoup = C.ContaPoupanca('0003', 'Simone de Almeida', '38475937495', 3000, 0.5)

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