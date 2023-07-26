MAIOR_IDADE = 18
#declaração da constante
IDADE_ESPECIAL = 12

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tirar habilitação!")

if idade < MAIOR_IDADE:
    print("Você é um bb, não pode ter habilitação.")
          
if idade == IDADE_ESPECIAL:
    print("você pode fazer as teóricas mais não as práticas")
    
else:
    print("opção inváalida")
# Aqui temos as tres condições, um verdadeira e a falsa ambas retornam uma mensagem, cada qual a seu respeito.
