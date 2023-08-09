import mysql.connector
from mysql.connector import errorcode
# from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='',
            password=''
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `caseBackend`;")

cursor.execute("CREATE DATABASE `caseBackend`;")

cursor.execute("USE `caseBackend`;")

# criando tabelas
TABLES = {}
TABLES['Cadastro'] = ('''
      CREATE TABLE `cadastro` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(200) NOT NULL,
      `sobrenome` varchar(200) NOT NULL,
      `idade` int NOT NULL,
      `pais` varchar(100) NOT NULL,          
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

# TABLES['Usuarios'] = ('''
#       CREATE TABLE `usuarios` (
#       `nome` varchar(20) NOT NULL,
#       `nickname` varchar(8) NOT NULL,
#       `senha` varchar(100) NOT NULL,
#       PRIMARY KEY (`nickname`)
#       ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# # inserindo usuarios
# usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
# usuarios = [
#       ("Carlos Alberto", "CA", generate_password_hash("car").decode('utf-8')),
#       ("João Ferreira", "JF", generate_password_hash("joa").decode('utf-8')),
#       ("Cesar Polvilho", "CP", generate_password_hash("ces").decode('utf-8'))
# ]
# cursor.executemany(usuario_sql, usuarios)

# cursor.execute('select * from caseBackend.usuarios')
# print(' -------------  Usuários:  -------------')
# for user in cursor.fetchall():
#     print(user[1])

# inserindo cadastro pessoais
cadastro_sql = 'INSERT INTO cadastro (nome, sobrenome, idade, pais) VALUES (%s, %s, %s, %s)'
cadastro = [
      ('Carlos ', 'Alberto', 37, 'Portugal'),
      ('João ', 'Ferreira', 28, 'Brasil'),
      ('Cesar ', 'Polvilho', 42, 'Chile'),
]
cursor.executemany(cadastro_sql, cadastro)

cursor.execute('select * from caseBackend.cadastro')
print(' -------------  Cadastro:  -------------')
for cadastro in cursor.fetchall():
    print(cadastro[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()