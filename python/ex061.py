n1 = float(input('Digite um número: '))
pa = float(input('Digite a razão do número: '))
cont = 0
print('A razão de \033[4;31m{}\033[m são: '.format(n1),end='')
while cont < 10:
    print('\033[4;31m', n1, '\033[m', end=', ')
    n1 = n1 + pa
    cont += 1
