# Implementação de um caixa eletrônico.

# Métodos.
def cadastro_usuario(usuarios):
    """Realiza o cadastro do usuário no sistema"""
    cpf = input("Informe o CPF [somente números]: ")
    
    if verifica_cpf(cpf,usuarios): # Retorna usuário caso o cpf esteja cadastrado.
        print("CPF já cadastrado, por favor tente novamente.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento [dd-mm-aaaa]: ")
    endereco = input("Informe o endereço [logradouro, nro - bairro - cidade/sigla estado]: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso.")

def verifica_cpf(cpf, usuarios):
    """Verifica se o cpf já está cadastrado no sistema, retornando o usuário"""
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario

def cadastro_conta(usuarios, contas, AGENCIA):
    """Realiza o cadastro da conta baseado no cpf do usuário"""
    numero_conta = len(contas) + 1
    cpf = input("Informe o CPF [somente números]: ")
    usuario = verifica_cpf(cpf, usuarios)
    
    if usuario:
        contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
        print("Conta cadastrada com sucesso.")
    
    else:
        print("CPF não cadastrado, por favor tente novamente.")

def deposito(valor, saldo, extrato, /):
        """Realiza operação de depósito"""
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor: .2f}\n"

        else:
            print("Depósito inválido, por favor tente novamente.")

        return saldo, extrato

def imprime_extrato(saldo, /, *, extrato):
    """Realiza operação de impressão de extrato"""
    print("============= Extrato =============")

    if not extrato: # variável está vazia.
        print("Não foram realizadas movimentações.\n")
    else:
        print(extrato)

    print(f"Saldo:    R${saldo: .2f}")
    print("===================================")
    
    return 

def saque(*, valor, saldo, extrato, numero_saques, LIMITE, LIMITE_SAQUES):
    """Realiza operação de saque"""
    if valor > LIMITE:
        print("Valor excede limite, por favor tente novamente.")

    elif numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques excedido.")

    elif valor > saldo:
        print("Saldo insuficiente, por favor tente novamente.")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:    R${valor: .2f}\n"

    else:
        print("Valor inválido, por favor tente novamente.")

    return saldo, extrato, numero_saques

# Variáveis e Parâmetros
menu = """Caixa Eletrônico - Operações
[0] Cadastro de Usuário
[1] Cadastro de Conta
[d] Depósito
[e] Extrato
[s] Saque
[q] Sair
Selecione a operação: """

usuarios = []
contas = []
extrato = ""
saldo = 0
numero_saques = 0

AGENCIA = "0001"    # Número da agência.
LIMITE = 500        # Valor máximo por saque.
LIMITE_SAQUES = 3   # Número de saques permitidos.

# Laço de Execução.
while True:
    opcao = input(menu)

    if opcao == "0":    # Cadastro de Usuário
        cadastro_usuario(usuarios)

    elif opcao == "1":  # Cadastro de Conta
        cadastro_conta(usuarios, contas, AGENCIA)
        
    elif opcao == "d":  # Depósito
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(valor, saldo, extrato)

    elif opcao == "s":  # Saque
        valor = float(input("Informe o valor de saque: "))
        saldo, extrato, numero_saques = saque(
            valor = valor,
            saldo = saldo,
            extrato = extrato,
            numero_saques = numero_saques,
            LIMITE = LIMITE,
            LIMITE_SAQUES = LIMITE_SAQUES
        )

    elif opcao == "e":  # Extrato
        imprime_extrato(saldo, extrato = extrato)
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor tente novamente.")

    print()

print("Volte Sempre!")