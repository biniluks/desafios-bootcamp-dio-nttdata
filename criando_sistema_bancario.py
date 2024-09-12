"""saldo = 0
extrato = ''
limite_valor_saque = 500
quantidade_saques = 0
limite_quant_saques = 3

menu = '''
Bem-vindo ao seu banco!
Selecione a opção desejada:

[1] - Depósito
[2] - Saque
[3] - Extrato
[0] - Sair

'''


while True:
    opcao = int(input(menu))
    if opcao == 1:
        deposito = float(input('Informe o valor do depósito: '))
        if deposito > 0:
            print('Depósito realizado com sucesso. Seu dinheiro já está disponível na conta!')
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
        else:
            print('\nValor insuficiente para realizar a operação')
    elif opcao == 2:
        saque = float(input('Digite o valor para realizar o saque: '))
        if saque > saldo:
            print('Você não possui saldo suficiente para completar a operação')
        elif saque > 0 and saque <= 500 and quantidade_saques < limite_quant_saques:
            print('Saque realizado com sucesso!')
            quantidade_saques += 1
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
        else:
            print('Não foi possível realizar a operação, por favor entre em contato com o seu gerente.\n')
    elif opcao == 3:
        print('\n=============== EXTRATO ===============')
        if extrato == '':
            print('Não foram realizadas movimentações')
            print(f'\nSaldo: R$ {saldo:.2f}')
            print('=======================================')
        else:
            print(extrato)
            print(f'\nSaldo: R$ {saldo:.2f}')
            print('=======================================')
    elif opcao == 0:
        print('Atendimento finalizado, obrigado por ser nosso cliente :)')    
        break
    else:
        print('Opção inválida, selecione outra opção.')"""

def deposito(saldo,valor,extrato,/):
    if valor <=0:
        print('Não é possível realizar o depósito')
    else:
        print('Depósito realizado com sucesso')
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
    return saldo, extrato
saldo = 0
extrato = ''

valor = float(input('Digite o valor do depósito: '))
saldo = deposito(saldo,valor,extrato)

print(saldo)
print(extrato)

print(extrato)