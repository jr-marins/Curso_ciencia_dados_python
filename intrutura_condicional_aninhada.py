conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 1000
cheque_esecial = 400
soma = saldo - saque
extrato = soma
opcao = -1

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso!")
        
    elif saque<= (saldo + chueque_especial):
        print("sauqe realizado com cheque especial")
    else:
        print("saldo insufuciente")
        
elif conta_universitaria:
    if saldo>=saque:
        print("saque realizado com sucesso!")
    else:
        print("saldo insuficiente")
        
else:
    print("Operação inválida, ou sistema não reconhce conta.\n Por favor entrar em contato com Banco de origem.")

if conta_normal == True and conta_universitaria == False:
#and(operador lógico E para inserir a condição )
    opcao = int(input("Sr desejar fazer mais operações, digite a opção desejada:\n[1]-Extrato\n[2]-Novo saque\n"))
#int para indicar e ler a entrada de um numero inteiro
    if opcao == 1:
        print("Seu saldo é de :\n$ ", extrato)
    
    elif opcao == 2:
        print("Digite o valor do saque:\n")
        
else:
    print()
    #incompleto, logo mais atualizações !
    
    


 