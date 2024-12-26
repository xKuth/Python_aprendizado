import random
n1 = random.randrange(0,5)
adivinhe = int(input('Qual o número aleatorio? '))
if n1 == adivinhe:
    print('número foi \033[4;33;40m{}\033[m !, Você acertou!'.format(n1))
else:
    print('O número foi \033[4;33;40m{}\033[m !,você errou tente novamente!'.format(n1))

#solução do Gustavo Guanabara

'''from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número \033[4;33;40m{}\033[m e não no \033[4;33;40m{}\033[m'.format(computador, jogador))'''
