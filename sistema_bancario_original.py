import textwrap

def menu():
    texto_menu = '''\n
    Digite a opção desejada:

    (1)\tDepositar
    (2)\tSacar
    (3)\tExtrato
    (4)\tNovo cliente
    (5)\tNova conta
    (6)\tListar contas
    (0)\tSair 
    '''
    return input(textwrap.dedent(texto_menu))

# Depositar sempre valor positivo, devem ser armazenados em uma variavel e exibidos no extrato
# Deve receber os argumentos apenas por porsição (positional only)
def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito:\tR$ {deposito:.2f}\n"
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
    else: 
        print("O valor do depósito não pode ser negativo.")
    return saldo, extrato    

# Sacar, realizar limite de 3 saques diarios com limite de 500, caso não tenha saldo, mensagem que nao sera possivel sacar, todos saques armazenados  para exibir operação extrato
# Deve receber os argumentos apenas por nomes (keyword only)
def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif saque > 0:
        saldo -= saque
        extrato += f"Saque:\t\tR$ {saque:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato
    
## Listar todos os depositos e saques realizados na conta.
def exibir_extrato(saldo, /, *, extrato):
        print("\n==================== EXTRATO ====================")
        print("Sem movimentações..." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================== FIM ======================")   

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do solicitante: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nCPF não encontrado, tente novamente!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    numero_saques = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            deposito = float(input("Digite o valor que deseja depositar: R$ "))
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == "2":
            saque = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
            saldo=saldo,
            saque=saque,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

main()
