from mysql import connector
cars = []
veiculos_real = []
comparacao = []
db = connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='cadastro'
)

table = db.cursor()
# table.execute('ALTER TABLE fabricantes add column carros VARCHAR(50) not null')

with open('cars_nissan.txt', 'r') as carros:
    for veiculos in carros:
        cars.append(veiculos)

for i, veiculos in enumerate(cars):
    carros = veiculos.strip('Nissan \n')
    veiculos_real.append(carros)

comparacao = ','.join(veiculos_real)

for i in range(len(veiculos_real)):
    valor = [comparacao]
    table.execute(f'Update fabricantes set nomes = %s where id = 33',  valor)

db.commit()
table.close()
db.close()
