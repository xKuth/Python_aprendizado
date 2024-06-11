def aumentar(num=0):
    aum = (num * 0.10) + num
    return aum


def diminuir(num=0):
    dim = num - (num * 0.13)
    return dim


def dobro(num=0):
    do = num * 2
    return do


def metade(num=0):
    me = num / 2
    return me


def moeda(num, moeda='R$'):
    novo_numero = f'{moeda}{num}'
    formatado = novo_numero.replace('.', ',')
    return formatado

