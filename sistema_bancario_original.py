menu = '''

Digite a opção desejada:

(1) Depositar
(2) Sacar
(3) Extrato
(0) Sair 

'''
saldo = 0
limite_saque = 500
limite_diario = 0
extrato = ""

while True:

    opcao = int(input(menu))

# Depositar sempre valor positivo, devem ser armazenados em uma variavel e exibidos no extrato
    if opcao == 1:
        deposito = float(input("Digite o valor que deseja depositar: R$ "))
        if deposito > 0:
            saldo = deposito + saldo
            extrato = extrato + f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
        else: 
            print("O valor do depósito não pode ser negativo.")

# Sacar, realizar limite de 3 saques diarios com limite de 500, caso não tenha saldo, mensagem que nao sera possivel sacar, todos saques armazenados  para exibir operação extrato
    if opcao == 2:
        if limite_diario < 3:
            saque = float(input("Digite o valor a ser sacado: R$ "))
            if saque > 0:
                if saque <= saldo:
                    if saque <= limite_saque:
                        saldo = saldo - saque
                        extrato = extrato + f"Saque: R$ {saque:.2f}\n"
                        limite_diario = limite_diario + 1
                        print(f"Este é o seu {limite_diario}º saque.")
                        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
                    else:
                        print("Valor excedido. Limite máximo de R$ 500 por saque.")
                else:
                    print(f"Sem saldo disponivel. Seu saldo é: R$ {saldo:.2f}.")
            else:
                print("O valor do saque não pode ser negativo.")
        else:
            print("Seu limite é de 3 saques diários.")

# Listar todos os depositos e saques realizados na conta.
    if opcao == 3:
        print("\n==================== EXTRATO ====================")
        print("Sem movimentações..." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================== FIM ======================")

    if opcao == 0:
        break

    else:
        print("Digite uma operação válida...")