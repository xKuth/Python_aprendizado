import mysql.connector
import random

connect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='cadastro',
)

table = connect.cursor()
# table.execute("alter table game add column valores int (3)"
# table.execute("alter table game modify column valores float(3) not null")
for i in range(1, 200):
    num_aleatorio = random.uniform(0, 100)
    table.execute(f"UPDATE game set valores = (%s) where id = (%s)", (num_aleatorio, i))

connect.commit()

table.close()
connect.close()
