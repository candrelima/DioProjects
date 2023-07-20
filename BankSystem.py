menu = '''
    ===== BankSystem_v1.0 =====
    [d] Depositar/Deposit
    [s] Sacar/Withdraw
    [e] Extrato/Bill
    [q] Sair/Quit

    =>>> Escolha uma operação: '''
saldo = 0
limite = 500
TOTAL_SAQUES = 3
n_saques = 0
extrato = '''
    === Movimetações - Depósitos ===
    '''
n_movimentacao = 0
while True:
    try:
        print(menu)
        op = input()

        if len(op) > 1:
            print('Opcão inválida.')
            continue

        if op == 'd':
            deposito = float(input('Quanto deseja depositar? R$ '))
            if deposito <= 0:
                print('Digite apenas valores válidos.')
                continue
            else:
                n_movimentacao += 1
                saldo += round(deposito, 2)
                extrato += f'   {n_movimentacao} - Deposito realizado -> R$ {deposito}\n'
                print(f'''      Saldo atualizado -> R$ {saldo}
                    ''')
                print(f'Deposito realizado -> R$ {deposito}')
                continue

        if op == 's':
            n_saques += 1
            if n_saques > TOTAL_SAQUES:
                print('Total de saques díario excedido.')
            else:
                saque = float(input('Quanto deseja sacar? R$ '))
                if saque > saldo:
                    print('Saldo insuficiente.')
                else:
                    if saque > limite:
                        print('Limite de saque excedido.')
                    elif saque <= saldo:
                        n_movimentacao += 1
                        saldo -= round(saque, 2)
                        extrato += f'{n_movimentacao} - Saque realizado -> R$ {saque}\n'
                        print(f'{n_movimentacao} - Saque realizado -> R$ {saque}')
                        print(f'''  Saldo atualizado -> R$ {saldo}
                            ''')
                continue

        if op == 'e':
            if n_movimentacao == 0:
                print('Não houve movimentações na conta.')
                continue
            print(extrato)
            print(f'''  Saldo atualizado -> R$ {saldo}
                ''')
            continue

        if op == 'q':
            print('Obrigado pela preferência.\nVolte sempre!\n\n\n')
            break
    except ValueError:
        print(f'Console com erro: {ValueError}')

