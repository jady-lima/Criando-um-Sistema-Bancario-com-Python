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
        print("d")
        break

    elif opcao == "s":
        print("s")
        break

    elif opcao == "e":
        print("e")
        break

    elif opcao == "q":
        print("q")
        break

    else:
        print("Nenhuma opção selecionada")
        break
