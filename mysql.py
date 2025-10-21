'''import pymysql

try:
    conexao = pymysql.connect(
        host="localhost",
        database="etecbd",
        user="root",
        password=" ",
        port=3306,
    )
    cursor = conexao.cursor()

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

        except pymysql.connector.Error as e: 
            print(f"Erro ao inserir dados: {e}")
            conexao.rollback()

        continuar = input("Deseja continuar? (s/n) ")
        if continuar.lower() == "n":
            break

  
    cursor.execute("SELECT * FROM Cadastro") 
    registros = cursor.fetchall()

    for row in registros:
        print("Nome = ", row[0]) 
        print("Sobrenome = ", row[1])
        print("Idade = ", row[2])
        print("Sexo  = ", row[3], "\n")

except pymysql.Error as e:
    print(f"Erro de conexão/operação com o banco de dados: {e}")

finally:
    print("Programa finalizado")
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
'''

# 1. Importar a nova biblioteca
import pymysql

# Inicialize as variáveis de conexão como None
conexao = None
cursor = None

try:
    # 2. Conecte-se usando pymysql.connect()
    conexao = pymysql.connect(
        host="localhost",
        database="etecbd",
        user="root",
        password="",  # Senha vazia do XAMPP
        port=3306,
        cursorclass=pymysql.cursors.DictCursor  # Um bônus: isso retorna dicionários em vez de tuplas
    )
    
    print("Conexão estabelecida com sucesso (usando PyMySQL)!")
    cursor = conexao.cursor()

    while True:
        # Leitura dos dados do usuário
        nome = input("Digite o nome do Cliente: ")
        estado = input("Digite o Estado (UF): ")
        sexo = input("Digite o Sexo (M/F): ").upper()
        status = input("Digite o Status: ")

        # Inserção no banco de dados
        try:
            sql = "INSERT INTO Clientes (Cliente, Estado, Sexo, Status) VALUES (%s, %s, %s, %s)"
            valores = (nome, estado, sexo, status)
            
            cursor.execute(sql, valores)
            conexao.commit()  # Confirma a inserção no banco
            print(f"Cliente '{nome}' inserido com sucesso! ID: {cursor.lastrowid}")

        # 3. Mudar para pymysql.Error
        except pymysql.Error as err:
            print(f"Erro ao inserir dados: {err}")
            conexao.rollback() # Desfaz a operação em caso de erro

        continuar = input("Deseja inserir outro cliente? (s/n): ")
        if continuar.lower() != "s":
            break

    # Consulta dos dados (após o loop de inserção)
    print("\n--- Exibindo todos os clientes cadastrados ---")
    cursor.execute("SELECT * FROM Clientes")
    registros = cursor.fetchall()

    # Como usamos DictCursor, podemos chamar por nome da coluna
    for row in registros:
        print(f"ID = {row['IDCliente']}, Cliente = {row['Cliente']}, Estado = {row['Estado']}, Sexo = {row['Sexo']}, Status = {row['Status']}\n")

# 3. Mudar para pymysql.Error
except pymysql.Error as err:
    # Captura erros de conexão ou de operações SQL
    print(f"Erro de conexão/operação com o banco de dados: {err}")

finally:
    # Garante que o cursor e a conexão sejam fechados
    print("Finalizando o programa.")
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()