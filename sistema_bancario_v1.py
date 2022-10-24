menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
LIMITE = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    # Deposito
    if opcao == 'd':
        valor_deposito = int(input('Quanto deseja depositar?\n'))
        saldo += valor_deposito
        print('Seu depósito foi realizado com sucesso!')
        extrato.append(f"Você realizou um depósito de R$ {saldo:.2f} reais.")
    
    # Saque
    elif opcao == 's':
        valor_sacado = int(input('Quanto deseja sacar?\n'))
        if numero_saques >= LIMITE_SAQUES:
            print('Você não pode mais sacar hoje. Seu limite foi atingido!!')
        elif valor_sacado > saldo:
            print('Não é possível sacar por falta de saldo!')
        elif valor_sacado > LIMITE:
            print('O limite de saque é de R$ 500.00 reais!')
        else:
            numero_saques+=1
            saldo -= valor_sacado
            extrato.append(f'Você realizou um saque de R$ {valor_sacado:.2f} reais.')
            print('Seu saquei foi realizado com sucesso!')
            
    # Extrato
    elif opcao == 'e':
        if len(extrato) == 0:
            print('Não foram realizadas movimentações!')
        else:
            print(' EXTRATO '.center(50,'-'))
            for i in extrato: print(i)
            print(f'Seu saldo atual é de {saldo:.2f}')

    elif opcao == 'q':
        break
    else:
        print('Operação inválida! Por favor selecione a opção desejada.')
