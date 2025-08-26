numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 >= 6 or numero2 >= 6:
    if numero1 > numero2:
        print(f"Este número é maior: {numero1}")
    else:
        print(f"Este número é maior: {numero2}")
elif numero1 < 5 and numero2 < 5:
    print("Os dois números são menores que 5.")
else:
    print("Pelo menos um dos números está entre 5 e 6.")