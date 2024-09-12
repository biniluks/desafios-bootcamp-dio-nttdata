def menu():
    menu='''
    Bem-vindo ao seu banco!
    Selecione a opção desejada:

    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [4] - Abrir conta

    [0] - Sair

    '''
    return input((menu))
def deposito(saldo,valor,extrato,/):
    if valor <=0:
        print('Não foi possível realizar o depósito, valor insuficiente para operação')
    else:
        print('Depósito realizado com sucesso')
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        return (saldo), extrato


saldo = 0
extrato = ''
limite_valor_saque = 500
quantidade_saques = 0
contas=[]

while True:
    opcao = int(menu())
    if opcao == 1:
        valor = float(input('Digite o valor do depósito: '))
        saldo, extrato = deposito(saldo,valor,extrato)
    else:
        break
    print(saldo)
    print(extrato)
