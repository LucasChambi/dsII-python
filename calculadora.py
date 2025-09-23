# Lucas Bruno Calle Chambi 3DS

# calculadora simples em Python
def calculadora():

    # .strip() remove espaços em branco extras, prevenindo erros.
    operacao = input("Digite uma operação (+, -, *, /): ").strip()
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        return

    # Funções para cada operação matemática
    def adicao(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        if b == 0:
            print("Erro: Divisão por zero não é permitida.")
            return None # retorna um valor nulo para indicar o erro
        return a / b

    operacoes = {
        '+': adicao,
        '-': subtracao,
        '*': multiplicacao,
        '/': divisao
    }

    if operacao in operacoes:
        # chama a função correspondente e armazena o resultado
        resultado = operacoes[operacao](num1, num2)
        if resultado is not None: # caso a operação obter um resultado que não seja nulo.
            print(f"O resultado da operação é: {resultado}")
    else:
        print("Operação inválida. Por favor, digite uma das seguintes: +, -, *, /")
        
calculadora()