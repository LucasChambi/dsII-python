
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
media = (numero1 + numero2) / 2

if int(media) % 2 == 0:
    print(f"O número {media} é par")
else:
    print(f"O numero {media} é impar")