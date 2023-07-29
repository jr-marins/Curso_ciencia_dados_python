nome = "marcos"
idade = 24
profissao ="programador"
linguagem = "python"
saldo = 38.556
#concatenando meu codigo

dados = {'nome': 'marcos','idade': 24, 'profissao': 'programador', 'linguagem': 'pyhon'}
#meu dicionario

print(" nome? \n%s\n idade? \n%d\n trabalha como ?\n%s\n estuda alguma linguagem? \n%s\n" % (nome, idade, profissao, linguagem))

print(" nome? {}\n idade? {}\n trabalha como ? {}\n estuda alguma linguagem? {}\n".format(nome, idade, profissao, linguagem))

print(" nome? {3}\nidade? {2}\ntrabalha como ? {1}\nestuda alguma linguagem? {0}\n".format(linguagem, profissao, idade, nome))

print(" nome? {nome}\n idade?: {idade}\n profissao: {profissao}\n linguagem: {linguagem}\n ".format(**dados))
#usando dados

print(f" nome? {nome}\n idade? {idade}\n trabalha como ? {profissao}\n estuda alguma linguagem? {linguagem}\n".format(nome, idade, profissao, linguagem))
#usando format

print(f" nome? {nome}\n idade? {idade}\n trabalha como ? {profissao}\n estuda alguma linguagem? {linguagem}\n saldo{saldo:20.1f}")
#Aqui ele conta as casas da direita para esquerda, eu pedi uma casa depois da letra f. Ele me retornou o 6 pois é a primeira casa da direita para esquerda