nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
divisor = 2

media = (nota1 + nota2) / divisor

if media >= 6:
    print("Aprovado")

elif media >=4 and media <= 5:
    print("Recuperação")
    
else:
    print("Reprovado")