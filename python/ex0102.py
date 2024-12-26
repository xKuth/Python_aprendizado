'''def fatorial(num, **mostrar):
    """
    :param num: Para calcular o fatorial do número digitado
    :param mostrar: Se Falso: ele não o calculo, if Verdadeiro: ele mostra
    """
    calculo = num
    valor = 0
    print('-='*20)
    if not mostrar:
        for cont in range(num-1, 1, -1):
            calculo *= cont
        print(calculo)
    elif mostrar:
        print(f'{calculo} x ', end='')
        for cont in range(num-1, 0, -1):
            calculo *= cont
            print(f'{cont}', end=' x ' if cont != 1 else ' = ')
        print(calculo)


print(help(fatorial))'''

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)
