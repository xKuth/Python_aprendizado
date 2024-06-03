from time import sleep
um = 1


def contador(inicio, fim, passo):
    if passo == 0:
        print(f'Contando de {inicio} ate {fim} de {um} em {um}')
        for cont in range(inicio, fim, um):
            sleep(0.3)
            print(cont, end=' ')
        print('FIM!')
    elif inicio < fim:
        print(f'Contando de {inicio} ate {fim} de {passo} em {passo}')
        for cont in range(inicio, fim, passo):
            sleep(0.3)
            print(cont, end=' ')
        print('FIM!')
    elif passo <= -1:
        print(f'Contando de {inicio} ate {fim} de {passo} em {passo}')
        for cont in range(inicio, fim, passo):
            sleep(0.3)
            print(cont, end=' ')
        print('FIM!')
    elif inicio > fim:
        print(f'Contando de {inicio} ate {fim} de -{passo} em -{passo}')
        for cont in range(inicio, fim, -passo):
            sleep(0.3)
            print(cont, end=' ')
        print('FIM!')


print('-='*30)
print('Contagem ate 10 de 1 em 1!')
for cont in range(1, 11):
    sleep(0.3)
    print(cont, end=' ')
print('FIM!')
print('-='*30)
print('Contagem de 10 ate 0 de 2 em 2!')
for cont in range(10, 0, -2):
    sleep(0.3)
    print(cont, end=' ')
print('FIM!')
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
contador(inicio=int(input('Inicio: ')), fim=int(input('Fim: ')), passo=int(input('passo: ')))
print()

'''# Solução do Gustavo Guanabara
from time import sleep


def contador(i, f, p):
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = 1
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')


# programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)'''

