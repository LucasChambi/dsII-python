# Criando uma lista com elementos
numeros = [1,2,3,4,5]
print(numeros[1])

# Criando uma lista com elementos de diferentes tipos de dados
lista_mista = [1, "String", 3.2]
print(lista_mista[2])

# Criando uma lista com outra lista dentro dela
lista_aninhada = [[1,2,3], [4,5,6], [7,8,9]]
print(lista_aninhada[1][2], lista_aninhada[2][1])

# Quando crio uma lista, posso armazenar varios tipos de dados, seja int, float, string, etc...
#ja na variavel, posso armazenar apenas um dado.

numeros = [1,2,3,4,5]
x = numeros[3]
print(numeros[x])

# com input
lista = []

x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
z = int(input("Digite um número: "))

lista.append(x)
lista.append(y)
lista.append(z)

print(lista)

# Fazendo um método diferente tirando as variaveis
lista = []

lista.append(int(input("Digite um número: ")))
lista.append(int(input("Digite um número: ")))
lista.append(int(input("Digite um número: ")))

print(lista)

# append quando adicionamos um numero inteiro, ele sempre será adicionado na ultima posição depois de uma lista
lista_incluida = [1,2,3]
lista_incluida.append(1) #ficará na ultima posição
print(lista_incluida)

# Criando outro método
lista_incluida = [[1,2], [3,4], [5,6]]
lista_incluida[0].append(9)
print(lista_incluida)

#Com Insert (qual posição quero inserir o valor)
lista = [1,2,3]
lista.insert(1, 4)
print(lista)

# for in
lista = [1,2,3,4,5]
for n1 in lista:
    print(n1) 

for n1 in range(10):
    print(n1)