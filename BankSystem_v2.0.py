

def deposito(saldo=0, valor=0, extrato='', n_movimentacao=0):
    try:
        n_movimentacao += 1
        saldo += round(valor, 2)
        print(f'''    ->    Deposito realizado -> R$ {valor}''')
        print(f'''    ->    Saldo atualizado -> R$ {saldo}''')
        extrato += f'''    ->    {n_movimentacao} - Deposito realizado -> R$ {valor}\n'''
    except NameError:
        print(f'Error: {NameError}')
        
    return saldo, extrato, n_movimentacao
#####################################

def sacar(*,saldo=0.0, valor=0.0, extrato='', limite=0, n_saques=0, limite_saques=0, n_movimentacao=0):
    try:
        if n_saques > limite_saques:
            print('''    ->    Total de saques díario excedido.''')
        else:
            if valor > saldo:
                print('''    ->    Saldo insuficiente.''')
            else:
                if valor > limite:
                    print('''    ->    Limite de saque excedido.''')
                else:
                    n_movimentacao += 1
                    saldo -= round(valor, 2)
                    print(f'''    ->    Saque realizado -> R$ {valor}''')
                    print(f'''    ->    Saldo atualizado -> R$ {saldo}''')
                    n_saques += 1
                    extrato += f'''    ->    {n_movimentacao} - Saque realizado -> R$ {valor}\n'''
    except NameError:
        print(f'Error: {NameError}')

    return saldo, extrato, n_saques, n_movimentacao
#####################################

def visualizarExtrato(saldo, *, extrato='', n_movimentacao=0):
    if n_movimentacao == 0:
        print('''    ->    Não houve movimentações na conta.''')
    else:
        print(extrato)
        print(f'''    ->    Saldo atualizado -> R$ {saldo}
            ''')
#####################################

#####################################           
def criarUsuario(nome='', nasc='', cpf='00000000000', lista_endereco={}):
    try:
        usuarioCriado = False
        while not usuarioCriado:
            print(f'''    ->    Por gentileza {nome}, confira os dados:
            -> Data de Nacismento: {nasc}
            -> CPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}
            -> Endereço:
                -> Logradouro: {lista_endereco['logradouro']}
                -> Número: {lista_endereco['n_logradouro']}
                -> Complemeto: {lista_endereco['complemento']}''')
            op = input('''    ->    OS DADOS ESTÁO CORRETOS? s - SIM / n - NÃO\n    ->    ''')

            if op.lower() == 's':
                usuarioCriado = True
                return usuarioCriado
            elif op.lower() == 'n':
                print('''    ->  **APENAS s - PARA SIM / n - PARA NÂO\n''')                

    except NameError:
        print(f'NameError: {NameError}')
#####################################

def criarConta(nome='', cpf='', endereco={}): # vincular ao usuario
    try:
        # buscar o numero da ultima conta
        total_contas = buscarTotalContasClientes(listaContas)
        conta = total_contas + 1
        # armazenar a conta
        print(f'''    ->    Conta: {conta}/Agência: {AGENCIA} foi criada com sucesso.''')
        criada = armazenarConta(nome, cpf, endereco, conta, AGENCIA)
        if criada:
            return conta
    except NameError:
        print(f'NameError: {NameError}')
        return False
#####################################

def armazenarConta(nome, cpf, endereco, conta, agencia='0001'):
    new_conta = {}
    new_conta['nome_usuario'] = nome
    new_conta['cpf'] = cpf
    new_conta['endereco'] = endereco
    new_conta['conta'] = conta
    new_conta['agencia'] = agencia
    listaContas.append(new_conta)
    if new_conta:
        return True
#####################################

def buscarTotalContasClientes(lista_contas):
    total_contas = 0
    for c in lista_contas:
            if len(c['cpf']) == 11:
                total_contas += 1
    #print(f"""    ->    Total de contas: {}""")
    return total_contas
#####################################

def buscarUsuario(cpf, lista_contas):
    print(f'''    ->====Nome========CPF========Conta/Agência''')
    for c in lista_contas:
        if c["cpf"] == cpf:
            print(f'''    ->    {c["nome_usuario"]}     {c["cpf"]}      {c["conta"]}/{c["agencia"]}''')
        else:
            print(f'''    ->   Sinto muito. Usuário inexistente.''')    
#####################################

def buscarConta(conta, lista_contas):
    print(f'''    ->====Conta========Nome========CPF''')
    for c in lista_contas:
        if c['conta'] == conta:
            print(f'''    ->    {c["conta"]}____{c["nome"]}____{c["cpf"]}''')
        else:
            print(f'''    ->   Sinto muito. Conta inexistente.''')  
#####################################

if __name__ == '__main__':
    
    menu = '''
    ===== BankSystem_v2.0 =====
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Cadastrar usuário
    [b] Buscar usuário
    [c] Buscar conta
    [q] Sair
    =>>> Escolha uma operação:'''

    AGENCIA = '0001'
    saldo = 1000
    limite = 500
    TOTAL_SAQUES = 3
    n_saques = 0
    extrato = '''    ============== Movimetações ==============\n'''
    movimentacoes = 0
    global listaContas
    listaContas = []

    while True:
        print(menu)
        op = input('''    ->    ''')
        user = ''

        if op[0] in ('d','s','e','n','b','c','q','D','S','E','N','B','C','Q'):
            #print('Valid entry.')
            op = op[0].lower()

            '============================================================='
            if op == 'd':
                dep = 0
                print(f'''    ->    Saldo R$ {saldo}''')
                try:
                    while dep < 1:
                        dep = float(input('''    ->    Quanto deseja depositar? R$ '''))
                except ValueError:
                    print('''->    Invalid entry.''')
                    continue
                # saldo, valor, extrato, n_movimentacao
                # retorno: saldo, extrato, n_movimentacao
                saldo, extrato, movimentacoes = deposito(saldo=saldo, valor=dep, extrato=extrato, n_movimentacao=movimentacoes)

            '============================================================='
            if op == 's':
                try:
                    valor = float(input('''    ->    Quanto deseja sacar? R$ '''))
                    while valor < 1:
                        valor = float(input('''    ->    Quanto deseja sacar? R$ '''))
                except ValueError:
                    print('''->    Invalid entry.''')
                    continue
                # dados = saldo, valor, extrato, limite, n_saques, limite_saques, n_movimentacao
                # retorno: saldo, extrato, n_saques, n_movimentacao
                saldo, extrato, n_saques, movimentacoes = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, n_saques=n_saques, limite_saques=TOTAL_SAQUES, n_movimentacao=movimentacoes)

            '============================================================='
            if op == 'e':
                # saldo, *, extrato, n_movimentacao
                # retorno: sem retorno
                visualizarExtrato(saldo, extrato=extrato, n_movimentacao=movimentacoes)

            '============================================================='
            if op == 'n':
                try:
                    usuario = {'nome':'', 'nascimento':'', 'cpf':'', 'lista_endereco':{}}
                    nome_usuario = input('''    ->    Nome do usuário: ''')

                    nascimento = input('''    ->    Digite a data de nascimento (apenas numeros): ''')
                    nascimento = f'{nascimento[0:2]}/{nascimento[2:4]}/{nascimento[4:6]}'

                    cpf = input('''    ->    Digite o CPF (apenas numeros): ''')
                    #cpf = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'

                    print('''->    PREENCHA O ENDEREÇO: ''')
                    logradouro = input('''->    Logradouro: ''')

                    n_logradouro = input('''->    Numero: ''')

                    complemento = input('''->    Complemento: ''')

                    usuario['nome_usuario'] = nome_usuario
                    usuario['nascimento'] = nascimento
                    usuario['cpf'] = cpf
                    usuario['lista_endereco']['logradouro'] = logradouro
                    usuario['lista_endereco']['n_logradouro'] = n_logradouro
                    usuario['lista_endereco']['complemento'] = complemento
                    # nome, nasc, cpf, lista_endereco
                    user = criarUsuario(nome=usuario['nome_usuario'],  nasc=usuario['nascimento'], cpf=usuario['cpf'], lista_endereco=usuario['lista_endereco'])
                    
                    if user:
                        print(f'''    ->    Usuário criado com sucesso.''')   

                    if user:
                        conta_criada = criarConta(usuario['nome_usuario'], usuario['cpf'], usuario['lista_endereco'])
                        if conta_criada:
                            print(f'''    ->    Conta: {conta_criada}/Agencia: {AGENCIA} cadastrada com sucesso.''')
                            print(f'''    ->    Conta: 000.{conta_criada} adicionada a base de dados.''')
                            #armazenarConta(usuario['nome'], usuario['cpf'], usuario['lista_endereco'], conta_criada, AGENCIA)     
                        else:
                            print(f'''    ->    Erro. Nenhuma conta encontrada.''')
                    else:
                        print('''    ->    Nenhum usuario associado para cadastrar uma conta.''')
                        
                except ValueError:
                    print('''->    Invalid entry.''')  

            '============================================================='
            if op == 'b':
                try:          
                    cpf = input('''    ->    Digite o CPF do usuário(apenas numeros): ''')
                    if len(cpf) != 11:
                        print('''    ->    Invalid entry. Try again.''')
                    else:
                        user = buscarUsuario(cpf, listaContas) # retorna o cpf do usuario
                        #print(user)
                        
                except ValueError:
                    print('''->    Invalid entry.''')
            
            '============================================================='
            if op == 'c':
                try:           
                    conta = input('''    ->    Digite o número da conta(apenas numeros): ''')
                    if not conta.isdigit():
                        print('''    ->    Invalid entry. Try again.''')
                    else:
                        user = buscarUsuario(cpf, listaContas) # retorna o cpf do usuario
                        #print(user)
                        
                except ValueError:
                    print('''->    Invalid entry.''')
            '============================================================='

            if op == 'q':
                print('''    ->    Obrigado pela preferência.\nVolte sempre!\n\n\n''')
                break
        else:
            print('''    ->    Invalid entry. Try again.''')