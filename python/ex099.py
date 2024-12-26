from time import sleep
from random import randint
numeros = []
aleatorio = indice = 0


def maior(*num):
    maiornumeros = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for cont in range(0, quant_numeros):
        aleatorio = randint(0, 9)
        sleep(0.3)
        print(aleatorio, end=' ')
        numeros.append(aleatorio)
    print(f'Foram informados {len(numeros)} valores ao todo')
    for i, cont in enumerate(numeros):
        if i == 0:
            maiornumeros = cont
        elif maiornumeros < numeros[i]:
            maiornumeros = cont
    print(f'O maior número foi {maiornumeros}')
    numeros.clear()


quant_numeros = 6
maior(quant_numeros)
quant_numeros = 3
maior(quant_numeros)
quant_numeros = 2
maior(quant_numeros)
quant_numeros = 1
maior(quant_numeros)
quant_numeros = 0
maior(quant_numeros)


