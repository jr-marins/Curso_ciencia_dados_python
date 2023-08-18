menu = f""" 
    Seja bem vindo ao ConsultBank, agradecemos pela preferência.
    
                        Digite a Opção desejada
             
    >>    [0] \tdepositar
    >>    [1] \tSacar
    >>    [2] \tExtrato
    >>    [3] \tnova conta
    >>    [4] \tlistar contas
    >>    [5] \tnovo usuário
    >>    [6] \tsair
    """

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"Seu depósito de : R$ {valor:.2f} foi realizado com sucesso !")

    else:
        print("\n Operação inválida !")

    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
     # Aqui tenho essas 3 verificaçoes, sobre a operação.
        excedeu_saldo = valor > saldo
    #Se o valor digitado for maior que o que o disponivel em saldo, opraçao incorreta    
        excedeu_limite = valor > limite
    #Se ultrapassou meu limite de 500, operação incorreta  
        excedeu_saques = numero_saques >= LIMITE_SAQUES
     #Se excededu minha quantidade diaria de sauqe, operaçao negada   

        if excedeu_saldo:
            print("Operação não realizada, seu saldo não é suficiente.")

        elif excedeu_limite:
            print("Operação não realizada por segurança. Confira seu limite de saque.")

        elif excedeu_saques:
            print("Operação não realizada, saques serão permitidos entre 24 horas.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\tR$ {valor:.2f}\n"
            print("Saque realizado com sucesso !!")

        else:
            print("Operação inválida, tente novamente.")

        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n################### EXTRATO #####################\n")
    #Aqui fiz um menu para facilitar a compreensão    
    print("Nao foram realizadas movimentaçoes."if not extrato else extrato)
    #Aqui uso o if ternário para verificar a condiçao da conta
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("##################################################\n")
    

def novo_usuario(usuarios):
    cpf = input("Digite seu CPF:")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("Este usuário já tem o cpf cadastrado")
        return
    
    nome = input("Informe o nome completo:\n")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa):\n")
    endereco = input("Informe seu endereço (logradouro, nmr, bairro, cidade/sigla estado):\n")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado !===")

def filtar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário:\n")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("conta criada com sucesso!!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, criação de conta não realizada.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
          Agência:\t{conta['agencia']}
          C/C:\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
     

        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    

    while True:
        opcao = input(menu)
    
        if opcao == '0':
            valor = float(input("informe o valor do depósito:\n"))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == '1':
            valor = float(input("Informe o valor do saque:\n"))

            saldo, extrato = sacar (
                saldlo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES, 
             )
     
            
        elif opcao == '2':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == '3':
            novo_usuario(usuarios)

        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '6':
            break
         
        else:
            print("Opção inválida, por favor selecione novamente a opção desejada.")

    main()