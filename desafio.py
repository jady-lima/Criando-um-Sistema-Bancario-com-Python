menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Valor do depósito: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Não é possível realizar a operação com saldo negativo. Por favor, recomece a operação.")

    elif opcao == "s":
        saque = float(input("Valor do saque: "))
        
        if numero_saques < LIMITE_SAQUES:
            if saque <= 500:
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

    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print("-" * 25)
            print(f"{extrato}Saldo final: R$ {saldo}")
            print("-" * 25)

    elif opcao == "q":
        break

    else:
        print("Nenhuma opção selecionada. Por favor, selecione uma opção seguindo o menu.")
