import random
import mysql.connector
numeros_jogos = []
auxilir_comp = []
comparacao_num = []
j = []

# abre o arquivo e coloca 6 numeros aleatorios por indice na lista
with open('registro_jogos.txt', 'w') as registrar:
    for i in range(0, 1000):
        numeros_jogos.clear()
        for a in range(0, 6):
            numeros_jogos.append(random.randint(1, 60))
        auxilir_comp.append(numeros_jogos[:])

# Pega a lista pronta e retira os itens repitidos
    for ind, valu in enumerate(auxilir_comp):
        indice = 0
        cont = 0
        comp = valu[indice]
        indice += 1
        if indice == 6:
            indice = 0

# Analisa os numeros dentro do indice da lista
        for i in valu:
            if i == comp:
                cont += 1
                if cont == 2:
                    auxilir_comp[ind].remove(comp)
                    auxilir_comp[ind].append(random.randint(1, 60))
                    cont -= 1

    registrar.write(f'Numeros sorteados: {"\n" * 2}')

    for i in range(len(auxilir_comp)):
        for e in range(0, 6):
            # Adiciona ao txt com espaço se não verifica se esta no ultimo indice para não adicionar espaço indesejado
            if not e == 5:
                numero_sorteado = str(auxilir_comp[i][e]) + ' '
                registrar.write(numero_sorteado)
            else:
                numero_sorteado = str(auxilir_comp[i][e])
                registrar.write(numero_sorteado)
        registrar.write('\n')

# Inicia a conexão com o banco de dados
connect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='cadastro'
)
connection = connect.cursor()
connection.execute('CREATE TABLE IF NOT EXISTS jogos (numeros_sorteados INT NOT NULL) ')

# abre o arquivo com números ja cadastrados
with open('registro_jogos.txt', 'r') as jogos:
    todos_jogos = jogos.read()
    # Retira os texto e os paragrafos indesejados
    n = todos_jogos.strip('Numeros sorteados:\n \n')
    r = n.split('\n')
    # Cria uma nova lista com os caracters organizados nos seus indices
    for i in r:
        j.append([i.replace(' ', ',')])
# Adiciona ao banco de dados a lista ja pronta
for i, element in enumerate(j):
    # Transforma a lista em uma string comum
    valor = element
    finish = valor[0]
    connection.execute('UPDATE jogos SET numeros_sorteados = (%s) WHERE id = (%s)', (finish, i))
# Confirma o envio ao banco de dados
connect.commit()
connect.close()
connection.close()
