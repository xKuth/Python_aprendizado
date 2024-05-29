numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n1 = 30
while True:
    while not n1 <= 20 or n1 > 0:
        n1 = int(input('Digite um número entre 0 e 20: '))
        if n1 > 20:
            print('Tente novamente. ', end='')
        else:
            break
    for cont in range(0, len(numeros)):
        if n1 == numeros[cont]:
            print(f'Você digitou o número \033[1;31m{contagem[cont]}\033[m')
    res = str(input('Quer continuar ? [S/N] ')).upper()[0]
    if res == 'N':
        break

# Solução do Gustavo Guanabara
'''cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o número {cont[num]}')'''