def soma(x, y):
    '''retorna a soma de dois números'''
    return x + y

def subtracao(x, y):
    '''retorna a subtração de dois numeros'''
    return x - y

def multiplicacao(x, y):
    '''retorna a multiplicação de dois numeros'''
    return x * y

def divisao(x, y):
    '''retorna o quociente da divisao de dois numero'''
    return x / y

def exp(x):
    '''retorna o expoente numeros'''
    return x ** 2

def raiz(x):
    '''retorna o expoente numeros'''
    return x ** 0.5

def memoria(resultado):
    '''armazena o resultado da ultima operação na memoria'''
    global ultima_operacao
    ultima_operacao = resultado

def mostrar_memoria():
    '''exibe o valor armazenado na memoria'''
    global ultima_operacao
    print(f"Valor na memória: {ultima_operacao}")

def main():
    '''executa a calculadora'''
    while True:
        #Exibe as opções de operação 
        print("-" * 20)
        print("**    Calculadora    **")
        print("-" * 20)
        print("| 1. Soma          |")
        print("| 2. Subtração     |")
        print("| 3. Multiplicação |")
        print("| 4. Divisão       |")
        print("| 5. Expoente      |")
        print("| 6. Raiz          |")
        print("| 7. Memória       |")        
        print("| 0. Sair          |")
        print("-" * 20)

opcao = int(input("Digite a opção desejada: "))

if opcao not in range(0, 8):
    print("Opção inválida!")
    continue

#executa a operação escolhida

elif opcao == 0:
    break

if opcao == 1:
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    resultado = soma(x, y)
    print(f"Resultado: {resultado}")
    memoria(resultado)

elif opcao == 2:
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    resultado = subtracao(x, y)
    print(f"Resultado: {resultado}")
    memoria(resultado)

elif opcao == 3:
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    resultado = multiplicacao(x, y)
    print(f"Resultado: {resultado}")
    memoria(resultado)

elif opcao == 4:
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    resultado = divisao(x, y)
    print(f"Resultado: {resultado}")
    memoria(resultado)

elif opcao == 5:
    x = float(input("Digite o primeiro número: "))
    # y = float(input("Digite o segundo número: "))
    resultado = exp(x)
    print(f"Resultado: {resultado}")
    memoria(resultado)

elif opcao == 6:
    x = float(input("Digite o primeiro número: "))
    # y = float(input("Digite o segundo número: "))
    resultado = raiz(x)
    print(f"Resultado: {resultado}")
    memoria(resultado)

elif opcao == 7:
    mostrar_memoria()

if __name__ == "__main__":
    main() 
    
# tratamento de except (evitar bugs)

def soma(x, y):
    try:
        return float(x) + float(y)
    except ValueError:
        print("Erro: valor inválido")

def subtracao(x, y):
    try:
        return float(x) - float(y)
    except ValueError:
        print("Erro: valor inválido")
        
def multiplicacao(x, y):
    try:
        return float(x) * float(y)
    except ValueError:
        print("Erro: valor inválido")
    
def divisao(x, y):
    try:
        return float(x) / float(y)
    except ValueError:
        print("Erro: valor inválido")
    except ZeroDivisionError:
        print("Zero não é divisivel")

def exp(x):
    try:
        return float(x) ** 2
    except ValueError:
        print("Erro: valor inválido")

def raiz(x):
    try:
        return float(x) ** 0.5
    except ValueError:
        print("Erro: valor inválido")


def main():
    while True:
        if opcao == 1:
            try:
                x = input("Digite o primeiro número: ")
                y = input("Digite o segundo número: ")
                resultado = soma(x, y)
            except ValueError:
                continue
            print("Resultado: {resultado}")
            memoria(resultado)

        if opcao == 2:
            try:
                x = input("Digite o primeiro número: ")
                y = input("Digite o segundo número: ")
                resultado = subtracao(x, y)
            except ValueError:
                continue
            print("Resultado: {resultado}")
            memoria(resultado)

        if opcao == 3:
            try:
                x = input("Digite o primeiro número: ")
                y = input("Digite o segundo número: ")
                resultado = multiplicacao(x, y)
            except ValueError:
                continue
            print("Resultado: {resultado}")
            memoria(resultado)

        if opcao == 4:
            try:
                x = input("Digite o primeiro número: ")
                y = input("Digite o segundo número: ")
                resultado = divisao(x, y)
            except ZeroDivisionError:
                continue
            print("Resultado: {resultado}")
            memoria(resultado)
            
        elif opcao == 0:
            break

        
if __name__ == "__main__":
    main()