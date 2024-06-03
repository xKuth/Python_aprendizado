


def aumentar(num):
    aum = (num * 0.10) + num
    return aum


def diminuir(num):
    dim = num - (num * 0.13)
    return dim


def dobro(num):
    do = num * 2
    return do


def metade(num):
    me = num / 2
    return me


def moeda(num):
    novo_numero = f'{num}'
    formatado = novo_numero.replace('.', ',')
    return formatado

