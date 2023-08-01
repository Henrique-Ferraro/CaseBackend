import pyodbc

connection = (
    "Driver={SQL Server};"
    "Server=LAPTOP-34N4CKPT\SQLEXPRESS;"
    "Database=caseBackend;"
)

con = pyodbc.connect(connection)
print("Conexao bem sucedida")

# Rodar comandos SQL
cursor = con.cursor()

sqlCommand = """INSERT INTO caseBackend(id, nome, sobrenome, idade, pais) 
VALUES 
    (1, 'Henrique', 'Ferraro', 37, 'Brasil')"""

cursor.execute(sqlCommand)