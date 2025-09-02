infantilA = int(input("Digite a sua idade: "))
infantilB = int(input("Digite a sua idade: "))
juvenilA = int(input("Digite a sua idade: "))
juvenilB = int(input("Digite a sua idade: "))
adultos = int(input("Digite a sua idade: "))

if infantilA >=5 and infantilA <= 7:
    print("Você faz parte da categoria Infantil A")
if infantilB >= 8 and infantilB <= 11:
    print("Você faz parte da categoria Infantil B")
if  juvenilA >= 12 and juvenilA <= 13:
    print("Categoria Juvenil A")
if juvenilB >= 14 and juvenilB <= 17:
    print("Categoria Juvenil B") 
if adultos > 18:
    print("Categoria Adultos")
else:
    print("Indisponivel")