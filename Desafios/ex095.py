gols = []
copia_gols = []
jogadores = []
while True:
    total = {'nome': str(input('Nome do jogador '))}
    partida = int(input(f'Quantas partidas {total['nome']} jogou? '))
    for cont in range(0, partida):
        gols.append(int(input(f'Quantos gols na patida {cont+1}º? ')))
    copia_gols.append(gols[:])
    total['gols'] = gols[:]
    soma = sum(gols[:])
    total['total'] = soma
    jogadores.append(total.copy())
    total.clear()
    gols.clear()
    res = str(input('Quer continuar ? [S/N] ')).upper()[0]
    if res == 'N':
        break
    print('-='*25)
print('-='*25)
print(f'{"Nº":<4}{"Nome":<10}{"Gols":<10}{"Total":<5}')
print('='*40)

for v in range(0, len(jogadores)):
    print(f'{v:<4}{jogadores[v]["nome"]:<10}', end='')
    contador = len(copia_gols[v])
    for i in range(0, len(copia_gols[v])):
        contador -= 1
        print(f'{copia_gols[v][i]:.<1}', end=',' if contador != 0 else '')
    print(f'{jogadores[v]["total"]:>8}')
print('='*20)
while True:
    while True:
        quant = int(input('Monstrar dados de qual jogador ? '))
        if quant == 999:
            break
        if quant > len(copia_gols):
            print(f'Erro! não exite jogador com codigo {quant}. digite novamente')
        else:
            break
    if quant == 999:
        break
    print(f'Levatamento do jogador {jogadores[quant]["nome"]}:')
    for cont in range(0, len(copia_gols[quant])):
        print(f'{"":<5}No jogo {cont+1} fez {copia_gols[quant][cont]} gols.')
    print('-'*30)
print('Finalizando...')



