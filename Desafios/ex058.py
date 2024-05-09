import random
comp_adiv = random.randrange(0, 10)
res = 0
cont = 0
while comp_adiv != res:
    res = int(input('Tenter adivinhar o meu número [0/10]:  '))
    if comp_adiv != res:
        print('Você errou o número que pensei tente novamente!!!')
        cont += 1
if cont >= 1:
    print('Programa finalizado você teve \033[1;31m{}\033[m tentativas erradas, você venceu no \033[1;31m{}\033[m palpite'.format(cont, cont+1))
else:
    print('O computador escolheu \033[1;31m{}\033[m e você \033[1;31m{}\033[m, Você acertou de primeira, parabens'.format(comp_adiv, res))
