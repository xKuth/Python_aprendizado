def aumentar(num, formataçao=False):
    """
    -> Retorna o valor aumentado
    :param num: valor entrada
    :param formataçao: se quer formatação com R$
    :return: valor aumentado com ou sem formaração
    """
    aum = (num * 0.10) + num
    if formataçao:
        formatado = moeda(aum)
        return formatado
    else:
        return aum


def diminuir(num, formataçao =False):
    dim = num - (num * 0.13)
    if formataçao:
        formatado = moeda(dim)
        return formatado
    else:
        return dim


def dobro(num, formataçao =False):
    do = num * 2
    if formataçao:
        formatado = moeda(do)
        return formatado
    else:
        return do


def metade(num, formatacao =False):
    me = num / 2   # Você tambem pode fazer inline: 'return me if not formatacao else moeda(me)
    if formatacao: # Ou return me if formatacao is false else moeda(me)
        formatado = moeda(me)
        return formatado
    else:
        return me


def moeda(num):
    novo_numero = f'R${num}'
    formatado = novo_numero.replace('.', ',')
    return formatado

