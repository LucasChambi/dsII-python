'''Irá printar a variável que está armazenada a lista'''
for n1 in [1,4,5,7,3]:
    print(n1)

'''---------------------------------------------------'''
lista = [4,34,34,23,2]
for n1 in lista:
    print(n1)

'''---------------------------------------------------'''
'''inicio, fim, por quanto vai cobrar'''
for n1 in range(1, 100, 2):
    print(n1)
    '''------------------------------------------'''
for n1 in [0,23, 43, 12, 32]:
    print(n1)
else:
    print("ACABOU!!!")
    '''-----------------------------------------'''
    for n1 in range(100000):
        print(n1)
        if n1 == 4:
            break # vai quebrar loop
        print("Até mais")
    '''------------------------------------'''
    numeros = [1,2,3,4,5]
    for numero in numeros:
        if numero == 10:
            break
        print(f"Número: {numero}")
    else:
        print("Acabou")