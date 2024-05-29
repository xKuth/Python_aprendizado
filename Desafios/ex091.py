from random import randint
jogadas = []
mai = []
registro_maior = 0
registro_menor = 0
for cont in range(0, 4):
    jogadores = {f'Jogada{cont}': randint(1, 6)}
    jogadas.append(jogadores)
    if cont == 0:
        mai.append(jogadas[cont])
        registro_maior = jogadas[cont][f'Jogada{cont}']
        registro_menor = jogadas[cont][f'Jogada{cont}']

    elif jogadas[cont][f'Jogada{cont}'] >= registro_maior:
        mai.insert(0, jogadas[cont])
        registro_maior = jogadas[cont][f'Jogada{cont}']

    elif jogadas[cont][f'Jogada{cont}'] <= registro_menor:
        mai.append(jogadas[cont])
        registro_menor = jogadas[cont][f'Jogada{cont}']
    else:
        mai.insert(cont-1, jogadas[cont])
print(mai)
print('Valores Sorteados:')
for cont in range(0, len(jogadas)):
    print(f'     O jogador{cont} tirou {jogadas[cont][f"Jogada{cont}"]}')
print(f'Ranking dos jogadores: ')

for cont in range(0, len(mai)):
    print(f'     {cont+1}º lugar: {mai[cont]} com {mai[cont].values()}')


# Solução do Gustavo Guanabara
'''from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1,6)}
ranking = list()
print('Valores sortedos')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)'''



