# Pede o ano de nascimento do usuário
nascimento = int(input("Digite o seu ano de nascimento (ex: 1990): "))
ano_atual = 2025 # pode alterar o ano
# Calcula a idade
idade = ano_atual - nascimento

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")