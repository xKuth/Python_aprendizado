'''def ficha(nome, gols):
    if len(jogador) > 0:
        print(f'O jogador {nome} fez ', end='')
    else:
        print(f'O jogador <Desconhecido> fez ', end='')
    if gols != '':
        print(f'{gols} gol(s) no campeonato')
    else:
        print(f'0 gol(s) no campeonato')


jogador = str(input('Nome do jogador: ')).strip()
numero = str(input('quantos gols ele fez: '))
ficha(jogador, numero)'''


# Solução do Gustavo Guanabara
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


n = str(input('Nome do jogador? '))
g = str(input('número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
