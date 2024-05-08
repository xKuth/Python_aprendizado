n1 = 0
n2 = 0
res = 0
matematica = 0
maior = 0
while res <= 4:
    print('-='*15)
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    print('-='*15)
    print('[1]Somar:\n[2]Multiplicar:\n[3]Maior\n[4]Novos números:\n[5]Sair do programa:\n')
    res = int(input(''))
    if res == 1:
        matematica = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, matematica))
    elif res == 2:
        matematica = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, matematica))
    elif res == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}'.format(maior))
    elif res == 4:
        print('Digite os novos números:')
    elif res == 5:
        print('Saindo do programa!')
    else:
        print('Erro Digite um comando correspodente de [1 ate 5]:')
        res = 0

