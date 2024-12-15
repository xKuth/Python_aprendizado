import mysql.connector
comparar = list()
marca_real = list()
marcas_carros = list()

conected = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='cadastro'

)
table = conected.cursor()
# table.execute("Drop table marcas")
table.execute("CREATE TABLE IF NOT EXISTS Fabricantes (id INT AUTO_INCREMENT PRIMARY KEY, nomes VARCHAR(50))")


with open('cars.txt', 'r') as carros:
    for i, marca in enumerate(carros):
        marcas_carros.append(marca)

valor = 0
for i in range(len(marcas_carros)):
    if i == 0:
        marca_real.append(marcas_carros[i])
    elif marcas_carros[i] != valor:
        marca_real.append(marcas_carros[i])
    valor = marcas_carros[i]

for i, letra in enumerate(marca_real):
    for o, letras in enumerate(letra):
        if letras == '\n':
            marca_real.remove('\n', o)

print(marca_real)


'''
for marca in marca_real:
    table.execute('Update Fabricantes set nomes = (%s)', marca)
conected.commit()
'''

