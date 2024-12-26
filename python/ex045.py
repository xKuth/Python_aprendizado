import random
lista = ['pedra', 'papel', 'tesoura']
comp_escolha = random.choice(lista)
print('Qual você quer jogar?\n[1]-Pedra\n[2]-Papel\n[3]-Tesoura')
jogo = int(input('Em qual você deseja jogar? (1 a 3): \n'))

if jogo == 1:
    jogador_escolha = 'pedra'
elif jogo == 2:
    jogador_escolha = 'papel'
elif jogo == 3:
    jogador_escolha = 'tesoura'

if (jogo >= 1) and (jogo <= 3):
    if (comp_escolha == 'pedra') and (jogo == 2) or (comp_escolha == 'tesoura') and (jogo == 1) or (comp_escolha == 'papel') and (jogo == 3):
      print('VOCÊ GANHOU')
      print('O computador jogou {}, e você jogou {}'.format(comp_escolha, jogador_escolha))
    elif comp_escolha == jogador_escolha:
        print('Jogo Empatado')
        print('O computador jogou {}, e você jogou {}'.format(comp_escolha, jogador_escolha))
    elif (comp_escolha == 'pedra') and (jogo == 3) or (comp_escolha == 'papel') and (jogo == 3) or (comp_escolha == 'tesoura') and (jogo == 1):
        print('Você perdeu')
        print('O computador jogou {}, e você jogou {}'.format(comp_escolha, jogador_escolha))


else:
    print('Numero digitado não correspondente , digite novamente!')

