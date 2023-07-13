# Implementação de um simples caixa eletrônico.
menu = """
Caixa Eletrônico - Operações
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Selecione a operação: """

extrato = ""
saldo = 0
numero_saques = 0
LIMITE = 500        # Valor máximo por saque.
LIMITE_SAQUES = 3   # Número de saques permitidos.

while True:
    opcao = input(menu)

    if opcao == "d":    # Depósito
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor: .2f}\n"

        else:
            print("Depósito inválido, por favor tente novamente.")

    elif opcao == "s":  # Saque
        valor = float(input("Informe o valor de saque: "))

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

    elif opcao == "e":  # Extrato
        print("============= Extrato =============")

        if not extrato: # variável está vazia.
            print("Não foram realizadas movimentações.\n")
        else:
            print(extrato)

        print(f"Saldo:    R${saldo: .2f}")
        print("===================================")        
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor tente novamente.")

print("Volte Sempre!\n")