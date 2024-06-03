def acessar():
    print('\033[1;32;40m~'*30)
    print(f'Acessando a biblioteca {biblioteca}')
    print('~'*30)


def msgsis():
    print('\033[1;34;40m~'*30)
    print('Sistema de ajuda Pyhelp')
    print('~'*30)


while True:
    biblioteca = str(input('Função ou biblioteca > '))
    if biblioteca in 'fim':
        break
    acessar()
    print('\033[m', '\033[7;32;40m')
    help(biblioteca)

    msgsis()
    print('\033[m')

print('\033[1;31;40m~'*20)
print(f'{"":^5}Até logo')
print('~'*20)
print('\033[m')
print()

# Solução do Gustavo Guanabara
'''from time import sleep
c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30'     # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('Sistema de ajuda Pyhelp', 2)
    comando = str(input('Funçao ou biblioteca'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
'''