def leiaint(txt):
    print(txt, end='')
    txt = input('')
    while txt[0] not in '1234567890':
        print('Erro! Digite um número inteiro válido.')
        txt = input('Digite um número: ')
    return txt


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

# Solução do gustavo Guanabara


'''def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mEroo! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
'''