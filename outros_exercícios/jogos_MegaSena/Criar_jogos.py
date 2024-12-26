import random
import mysql.connector
numeros_jogos = []
auxilir_comp = []


with open('registro_jogos.txt', 'w') as registrar:
    for i in range(0, 1000):
        numeros_jogos.clear()
        for a in range(0, 6):
            numeros_jogos.append(random.randint(1, 60))
        auxilir_comp.append(numeros_jogos[:])
    registrar.write(f'Numeros sorteados: {"\n" * 2}')
    for i in range(len(auxilir_comp)):
        for e in range(0, 6):
            numero_sorteado = str(auxilir_comp[i][e]) + ' '
            registrar.write(numero_sorteado)
        registrar.write('\n')

connect = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='1234',
    database ='cadastro'
)
connection = connect.cursor()
connection.execute('CREATE TABLE IF NOT EXISTS jogos (numeros_sorteados INT NOT NULL) ')
with open('registro_jogos.txt', 'r') as jogos:
    todos_jogos = jogos.read()
    n = todos_jogos.strip('Numeros sorteados: \n \n')
    r = n.split('\n')
for i in range(len(r)):
    valor = [r[i]]
    print(valor)
    connection.execute('INSERT INTO jogos (numeros_sorteados) VALUES (%s)', valor)

connect.commit()
connect.close()
connection.close()
