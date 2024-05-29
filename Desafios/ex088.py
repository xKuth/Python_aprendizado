from random import randint
from time import sleep
jogo = []
registro = contagem = 1
print('-='*25)
print(f'{'JOGO DA MEGA SENA':>22}')
print('-='*25)
numero_jogos = int(input('Quantos jogos quer que eu sorteie? '))
print(f'\033[1;33m{' SORTEANDO':=>23} {numero_jogos:^2}{'JOGOS ':=<19}\033[m')
for cont in range(0, numero_jogos):
    for rep in range(0, 6):
        jogo.append(randint(0, 60))
        registro = jogo[rep]
        if registro == jogo:
            jogo.pop()
            rep -= 1
    sleep(1)
    print(f'jogo {contagem}: {jogo}')
    contagem += 1
    jogo.clear()
print(f'{' < BOA SORTE! > ':=^45}')