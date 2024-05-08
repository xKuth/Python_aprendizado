n1 = float(input('Digite um número: '))
pa = float(input('Digite a razão do número: '))
cont = 0
res = 0
print('A razão de \033[4;31m{}\033[m são: '.format(n1), end='')
while cont < 10:
    print('\033[4;31m', n1, '\033[m', end=', ')
    n1 = n1 + pa
    cont += 1
    if cont == 10:
        print('\nVocê quer monstar mais quantos termos? \n[1 a 10]para mais termos: \n[0]para encerrar:\n')
        res = int(input(''))
        if res >= 1 and res <= 10:
            cont = cont - res
        elif res > 11:
            print('Erro! Digite o número correto! finalizando')
        elif res == 0:
            print('Finalizando')




