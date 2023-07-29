
nome = "marcos"
#Manipulando strings
print(nome.upper())
#todos os caracters em maiuscula
print(nome.lower())
#todoa es minuscula
print(nome.title())
#todos em minusculo exceto o primeiro caracter

texto = "   cortando os espaços    "

print(texto + ".")
print(texto.strip() + ".")
#Ambos os espaços

print(texto.lstrip() + ".")
#left(esquerda)

print(texto.rstrip() + ".")
#right(direita)

menu = "python"

print(menu.center(14))
#centraliza e os epeços acrescentados fica em branco
print(menu.center(14, "#"))
#cetralizada no meio de caracteres novos
print("_".join(menu))
#O caracter _ nao aparece depois do n porque n é o ultimo caracter.