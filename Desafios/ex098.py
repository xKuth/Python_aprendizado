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
