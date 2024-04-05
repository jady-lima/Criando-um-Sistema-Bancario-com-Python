import textwrap

LIMITE_SAQUES = 3
usuarios = []
contas = []

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def realizar_deposito(saldo, extrato):
    deposito = float(input("Valor do depósito: "))  
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
    else:
        print("Não é possível realizar a operação com saldo negativo. Por favor, recomece a operação.")

    return saldo, extrato

def realizar_saque(*, saldo, extrato, numero_saques, limite):
    saque = float(input("Valor do saque: "))
     
    if numero_saques < LIMITE_SAQUES:
        if saque <= limite:
            if saque <= saldo and saque > 0:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
                print("Saque efetuado com sucesso!")
            else:
                print("Não possivel efetuar o saque por falta de limite.")
        else:
            print("Saque maior que o limite permitido.")
    else:
        print("Limite de saque diário atingido")

    return saldo, extrato

def imprimir_extrato(extrato, /, *, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def novo_usuario():
    cpf = int(input("Digite seu CPF (somente números): "))

    if filtrar_usuario(cpf):
        print("Usuario já cadastrado")
        return
    
    else:
        nome = input("Informe seu nome completo: ")
        dataNascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        logradouro = input("Digite o Logradouro: ")
        numero = int(input("Agora, nos informe o número: "))
        bairro = input("Digite seu bairro: ")
        estado = input("Digite as siglas do estado que reside: ")
        user = {
            "nome": nome, 
            "dataNascimento": dataNascimento, 
            "cpf": cpf, 
            "endereco": {"logradouro": logradouro, "numero": numero, "bairro": bairro, "estado": estado},
            "saldo": 0.0
        }
        print("=== Usuário criado com sucesso! ===")
    
    usuarios.append(user)
    return user

def nova_conta_corrente(id_conta):
    usuario = novo_usuario()

    cont = {
        "agencia": "0001",
        "numero_conta": id_conta,
        "usuario": usuario
    }

    contas.append(cont)
    print("\n=== Conta criada com sucesso! ===")
    return id_conta + 1

def listar_contas():
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 35)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    id_contas = len(contas)

    while True:
        opcao = menu()

        if opcao == "d":
            retorno = realizar_deposito(saldo, extrato)
            saldo = retorno[0]
            extrato = retorno[1]

        elif opcao == "s":
            retorno = realizar_saque(saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite)
            saldo = retorno[0]
            extrato = retorno[1]

        elif opcao == "e":
            imprimir_extrato(extrato, saldo=saldo)

        elif opcao == "nc":
            id_contas = nova_conta_corrente(id_contas)

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            break
            
        else:
            print("Nenhuma opção selecionada. Por favor, selecione uma opção seguindo o menu.")

main()