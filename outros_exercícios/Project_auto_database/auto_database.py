import mysql.connector


connect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='cadastro',
)

table = connect.cursor()
table.execute("CREATE TABLE IF NOT EXISTS game (id INT PRIMARY KEY, personagem VARCHAR(50))")

for i in range(1, 200):
    personagem = f"nome{i}"
    table.execute("INSERT INTO game (id, personagem) VALUES (%s, %s)", (i, personagem))

connect.commit()

table.close()
connect.close()
