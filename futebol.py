# caminho de decisão

time1 = float(input("Informe a quantidade de gols: "))
time2 = float(input("Informe a quantidade de gols: "))

if time1 == time2:
    print("Deu empate")
elif time1 >=  time2:
    print(f"A vitoria é do time 1")
else: 
    print("O time 2 é o vencedor")