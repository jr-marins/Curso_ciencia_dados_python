
#Operadores lógicos com operadores de comparação.

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)
#Seguindo a tabela verdade em um programa bancario

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp)
