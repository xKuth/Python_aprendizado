import random
perder = jogada = s = comp_jogo = cont = 0
im_pa = identificador = ''
print('-='*15)
print('Vamos jogar Par ou Impar')
print('-='*15)
while perder < 1:
    comp_jogo = random.randrange(1, 10)
    jogada = int(input('Digite um valor: '))
    im_pa = str(input('Vai jogar Par ou Impar? [P/I] ')).upper()
    s = comp_jogo + jogada
    if s % 2 == 0:
        identificador = 'Par'
        print(f'Você jogou {jogada} e o computador jogou {comp_jogo}. O total deu {s} deu {identificador}')
    else:
        identificador = 'Impar'
        print(f'Você jogou {jogada} e o computador jogou {comp_jogo}. O total deu {s} deu {identificador}')
    if s % 2 == 0 and im_pa == 'P':
        cont += 1
        print('Você ganhou!')
        print('Vamos jogar novamente...\n', '-='*15)
    elif s % 2 == 1 and im_pa == 'I':
        cont += 1
        print('Você ganhou!')
        print('Vamos jogar novamente...\n', '-=' * 15)
    if s % 2 == 0 and im_pa == 'I':
        perder = 2
        print('Você perdeu')
        break
    elif s % 2 == 1 and im_pa == 'P':
        perder = 2
        print('Você perdeu')
        break
print('-='*15)
print(f'Game Over! Você vendeu {cont} vezes.')