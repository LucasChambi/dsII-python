valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite o valor da taxa que será cobrado: "))
tempo = float(input("Informe quantidade de meses atrasados: "))

prestacao = valor + (valor * (taxa/100) * tempo)
print("A prestação calculada foi :", prestacao)