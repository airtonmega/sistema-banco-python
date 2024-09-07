from datetime import datetime

# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Função para criar um usuário
def criar_usuario():
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe o CPF (somente números): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Verificar se o CPF já existe
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Já existe um usuário com este CPF.")
            return
    
    # Adicionar novo usuário à lista
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")

# Função para criar uma conta corrente
def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    agencia = "0001"
    numero_conta = len(contas) + 1

    # Procurar usuário pelo CPF
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado:
        conta = {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'usuario': usuario_encontrado,
            'saldo': 0,
            'limite': 500,
            'extrato': "",
            'numero_saques': 0,
            'LIMITE_SAQUES': 3
        }
        contas.append(conta)
        print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    else:
        print("Erro: Usuário não encontrado. Crie o usuário antes de abrir uma conta.")

# Função para listar as contas
def listar_contas():
    if contas:
        print("\n=== Listagem de Contas ===")
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")
        print("==========================\n")
    else:
        print("Nenhuma conta criada.")

# Função para listar os usuários
def listar_usuarios():
    if usuarios:
        print("\n=== Listagem de Usuários ===")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Endereço: {usuario['endereco']}")
        print("============================\n")
    else:
        print("Nenhum usuário cadastrado.")

# Função para acessar uma conta e realizar operações
def acessar_conta():
    cpf = input("Informe o CPF do usuário: ")
    numero_conta = int(input("Informe o número da conta: "))

    # Procurar conta
    conta_encontrada = None
    for conta in contas:
        if conta['usuario']['cpf'] == cpf and conta['numero_conta'] == numero_conta:
            conta_encontrada = conta
            break
    
    if conta_encontrada:
        menu_conta(conta_encontrada)
    else:
        print("Erro: Conta não encontrada!")

# Função para gerenciar as operações de uma conta
def menu_conta(conta):
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    
    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                conta['saldo'] += valor
                conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > conta['saldo']
            excedeu_limite = valor > conta['limite']
            excedeu_saques = conta['numero_saques'] >= conta['LIMITE_SAQUES']

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                conta['saldo'] -= valor
                conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
                conta['numero_saques'] += 1
                print("Saque realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
            print(f"\nSaldo: R$ {conta['saldo']:.2f}")
            print("==========================================")

        elif opcao == "q":
            print("Saindo da conta...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Função para o menu principal
def menu_principal():
    menu = """
    [1] Criar Usuário
    [2] Criar Conta Corrente
    [3] Acessar Conta
    [4] Listar Usuários
    [5] Listar Contas
    [6] Sair
    => """
    
    while True:
        opcao = input(menu)
        
        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            acessar_conta()
        elif opcao == "4":
            listar_usuarios()
        elif opcao == "5":
            listar_contas()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Escolha uma opção válida.")

# Iniciar o sistema
menu_principal()
