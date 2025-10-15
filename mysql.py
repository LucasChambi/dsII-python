import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost:3306",
        database="usuario",
        user="root",
        password=" ",  # Coloque a senha correta do root aqui
        port=3306,
        auth_plugin='mysql_native_password'  # Use isso APENAS se não puder alterar a autenticação no MySQL
    )
    cursor = conexao.cursor()

    # ... resto do seu código ...


    while True:
        nome = input("Digite o Nome: ")
        sobrenome = input("Digite o Sobrenome: ")
        idade = int(input("Digite a Idade: "))
        sexo = input("Digite o Sexo (M/F): ").upper()

        # Inserção
        try:
            cursor.execute("INSERT INTO Cadastro (Nome, Sobrenome, Idade, Sexo) VALUES (%s, %s, %s, %s)", (nome, sobrenome, idade, sexo))
            conexao.commit()
            print("Dados inseridos com sucesso!")

        except mysql.connector.Error as e: # Correção: mysql.connector.Error
            print(f"Erro ao inserir dados: {e}")
            conexao.rollback()

        continuar = input("Deseja continuar? (s/n) ")
        if continuar.lower() == "n":
            break

    # Consulta (após o loop de inserção)
    cursor.execute("SELECT * FROM Cadastro") # Nome da tabela corrigido
    registros = cursor.fetchall()

    for row in registros:
        print("Nome = ", row[0]) # Índices corrigidos
        print("Sobrenome = ", row[1])
        print("Idade = ", row[2])
        print("Sexo  = ", row[3], "\n")

except mysql.connector.Error as e: # Correção: mysql.connector.Error
    print(f"Erro de conexão/operação com o banco de dados: {e}")

finally:
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
