total = {'nome': str(input('Nome do jogador '))}
gols = []
partida = int(input('Quantas partidas ele jogou? '))
for cont in range(0, partida):
    gols.append(int(input(f'Quantos gols na patida {cont+1}º? ')))
total['gols'] = gols
soma = sum(gols)
total['total'] = soma
print('-='*25)
print(total)
print('-='*25)
for i, v in total.items():
    print(f'O campo {i} tem o valor {v}.')
print('-='*25)
print(f'O jogador {total['nome']} jogou {partida} partidas.')
for cont in range(0, len(gols)):
    print(f'{'':<7}=> Na partida {cont+1}, fez {gols[cont]} gols. ')
print(f'Foi um total de {total['total']} gols.')

# Solução do Gustavo Guanabara
'''jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')'''
