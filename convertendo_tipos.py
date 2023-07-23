print(int(1.0))
#aqui peço que ele me retorne o valor inteiro, então irá imprimir somente o 1.

print(float("10.10"))
#Ele ignora o 0 pois 10.10 e 10.1 para o float é a mesma coisa.

print(type(str(10.10)))
#Aqui ele retornará como uma string porem não dara para ver para qual tipo ele converteu, a não ser que eu coloque 'type' para perguntar qual a classe/tipo da variavel que ele me retorna.


# mesmo contexto do comentários de baixo.
print(int(1.986422537))
print(int("10"))
print(float("10.10"))
print(float(100))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))
#primeiiro ele disse que o valor é inteiro, depois ele dis que o valor é uma str.

#Agora em divisão, float em inteiro. ou vice versa
print(100 / 2)
#ele me retorna um valor float
print(100 // 2)
#ele me retorna um vallor inteiro.