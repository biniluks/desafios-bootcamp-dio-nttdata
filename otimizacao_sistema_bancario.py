def menu():
    menu = '''
Bem-vindo ao seu banco!
Selecione a opção desejada:

[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Cadastrar cliente
[5] - Abrir conta

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
        return saldo, extrato
def exibir_extrato(extrato,saldo):
    if extrato == '':
        print('============= EXTRATO =============')
        print('Não foram realizadas movimentações\n')
        print(f'Saldo:\tR$ {saldo:.2f}')
        print('===================================')
    else:
        print('============= EXTRATO =============')
        print(extrato)
        print(f'Saldo:\tR$ {saldo:.2f}')
        print('===================================')
def saque(valor,limite_valor_saque,limite_qtd_saques,saldo,extrato,quantidade_saques):
    if valor > saldo:
            print('Você não possui saldo suficiente')
    elif valor > 0 and valor <= limite_valor_saque and quantidade_saques < limite_qtd_saques:
        print('Saque realizado com sucesso')
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        quantidade_saques += 1
    else:
        print('Não foi possível realizar o saque. Entre em contato com o seu gerente')
    return saldo, extrato, quantidade_saques
def cadastro_clientes(cpf,clientes):
    filtro = [usuario for usuario in clientes if usuario['cpf']==cpf]
    if filtro:
        print('Usuário já cadastrado')
    else:
        nome = input('Digite seu nome completo: ')
        data_nascimento = input('Digite sua data de nascimento(XX-XX-XXXX): ')
        endereco = input('Digite seu endereço(Rua, nº - Bairro - Cidade/UF): ')
        clientes.append({'nome':nome,'data':data_nascimento,'cpf':cpf,'endereco':endereco})
def criar_conta(cpf,contas,clientes,agencia):
    filtro = [usuario for usuario in clientes if usuario['cpf']==cpf]
    if filtro:
        n_conta = len(contas) + 1
        contas.append({cpf:{'agencia':agencia,'n_conta':n_conta,}})
    else:
        print('O CPF informado não pertence a nenhum cliente cadastrado')

saldo = 0
extrato = ''
limite_valor_saque = 500
quantidade_saques = 0
limite_qtd_saques = 3
clientes = []
contas = []
agencia = '0001'

while True:
    opcao = int(menu())
    if opcao == 1:
        valor = float(input('Digite o valor do depósito: '))
        saldo, extrato = deposito(saldo,valor,extrato)
    elif opcao == 2:
        valor = float(input('Digite o valor para saque: '))
        saldo, extrato, quantidade_saques = saque(valor,limite_valor_saque,limite_qtd_saques,saldo,extrato,quantidade_saques)        
    elif opcao == 3:
        exibir_extrato(extrato,saldo) 
    elif opcao == 4:
        cpf = int(input('Digite seu CPF, apenas números: '))
        cadastro_clientes(cpf,clientes)
    elif opcao == 5:
        cpf = int(input('Digite seu CPF, apenas números: '))
        criar_conta(cpf,contas,clientes,agencia)
    else:
        print('Obrigado por ser nosso cliente :)')
        break