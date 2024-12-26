def leiaint(txt):
    print(txt, end='')
    valorst = str(input(''))
    while True:
        if valorst == '':
            break
        try:
            valor = int(valorst)
        except (ValueError, TypeError):
            print('\033[1;31mErro! por favor digite um numero inteiro\033[m')
            print(txt, end='')
            valorst = str(input(''))
        else:
            return valor
    if valorst == '':
        print('\033[1;31mO usuario preferiu não digitar esse número!\033[m')
        return 0


def leiafloat(txt):
    print(txt, end='')
    valorf = str(input(''))
    while True:
        if valorf == '':
            break
        try:
            valor = float(valorf)
        except(ValueError, TypeError):
            print('\033[1;31mErro! Por favor digite um número real\033[m')
            print(txt, end='')
            valorf = str(input(''))
        else:
            return valor
    if valorf == '':
        print('\033[1;31mO usuario preferiu não digitar esse número!\033[m')
        return 0


inteiro = leiaint('Digite um número inteiro: ')
real = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')


# Solução do gustavo Guanabara
'''def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Porfavor, digite um número inteiro valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsúario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Porfavor, digite um número inteiro valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsúario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um Inteiro: ')
n2 = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')'''
