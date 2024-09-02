menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    >>>> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para DEPÓSITO: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} realizado\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")       
        
    elif opcao == "s":
        valor = float(input("Informe o valor do SAQUE: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f} realizado \n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n============= EXTRATO ==============")
        print('''Não foram realizadas movimentações
      até o presente momento.''' if not extrato else extrato)
        print(f"\n====================================")
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("====================================")

    elif opcao == "q":
        print("Obrigado por ser nosso Cliente!!!")
        break

    else:
        print('''
            Operação inválida! 
            Por favor verifique a operação desejada.
            ''')
