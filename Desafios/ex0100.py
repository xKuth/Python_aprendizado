from random import randint
numero = []
soma = 0


def somapar(n1):
    print(f'Somando os valores pares de {numero}, temos: ', end='')
    for pares in numero:
        if pares % 2 == 0:
           n1 += pares
    print(n1)


def sorteia():
    print('Sorteando 5 numeros: ', end='')
    for cont in range(0, 5):
        numero.append(randint(0, 10))
        print(numero[cont], end=' ')
    print('Pronto!')


sorteia()
somapar(soma)
