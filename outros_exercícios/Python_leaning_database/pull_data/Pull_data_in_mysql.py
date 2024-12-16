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
# table.execute("alter table game add column comp_validada varchar(1) not null")
'''
for i in range(1, 200):
    num_aleatorio = random.uniform(0, 100)
    table.execute(f"UPDATE game set valores = (%s) where id = (%s)", (num_aleatorio, i))
'''

'''
for i in range(0, 200):
    escolhida = random.choice(['v', 'f'])
    table.execute("Update game set comp_validada = (%s) where id = (%s)", (escolhida, i))
'''
table.execute("select * from fabricantes")
resultado = table.fetchall()
for x in resultado:
    print(x)

# connect.commit()

table.close()
connect.close()

