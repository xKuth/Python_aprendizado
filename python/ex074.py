from random import randrange
print(f'Os valores sorteados foram: ', end='')
maior = menor = valor = 0
for cont in range(0, 5):
    n1 = randrange(0, 10)
    print(n1, end=' ' if cont < 4 else '\n')
    if cont == 0:
        maior = n1
        menor = n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
# Solução do Gustavo Guanabara
'''from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10), )
print('Os valores sorteados foram: ', end='')
for n in numeros:
        print(f'{n}', end=' ')
print(f'\no maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
'''