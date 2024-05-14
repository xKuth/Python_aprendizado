numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')
n1 = 30
while not n1 <= 20 or n1 > 0:
    n1 = int(input('Digite um número entre 0 e 20: '))
    if n1 > 20:
        print('Tetnte novamente. ', end='')
    else:
        break
for cont in range(0, len(numeros)):
    if n1 == numeros[cont]:
        print(f'Você digitou o número \033[1;31m{contagem[cont]}\033[m')
