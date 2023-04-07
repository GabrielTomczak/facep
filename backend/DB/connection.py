import mysql.connector

class DatabaseConnection(mysql.connector.connect):
  def __init__(self):
    super().__init__(
      host="localhost",
      user="username",
      password="password",
      database="database_name"
    )

db = DatabaseConnection()

# cursor = db.cursor()
# cursor.execute("SELECT * FROM tabela")
# resultado = cursor.fetchall()
# for linha in resultado:
#     print(linha)