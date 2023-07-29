menu = f""" 
    Seja bem vindo ao ConsultBank, agradecemos pela preferência.
    
                        Digite a Opção desejada
             
    >>    [0] depositar
    >>    [1] Sacar
    >>    [2] Extrato
    >>    [3] Sair
    """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    
    if opcao == '0':
        valor = float(input("informe o valor do depósito:\n"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou o valor informado é inválido\n")
        
    elif opcao == '1':
        valor = float(input("Informe o valor do saque:\n"))
        
    # Aqui tenho essas 3 verificaçoes, sobre a operação.
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Desculpa mais seu saldo é insuficiente.\n")
            
        elif excedeu_limite:
            print("O valor do saque excedeu o limite\n")
            break
            
        elif excedeu_saques:
            print("Você atingiu o limite de saques\n")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação invalida")
        
    elif opcao == '2':
        print("\n################### EXTRATO #####################\n")
        print("Nao foram realizadas movimentaçoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###################################################\n")
        
        
    elif opcao == '3':
        break

else:
    print("Opção inválida, por favor selecione novamente a opção desejada.")