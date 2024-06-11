def resumo(num, a, b):
    dobro = num * 2
    metade = num / 2
    aumento = ((num / 100) * a) + num  # aumnetar porcetagem
    reduçao = num - ((num / 100) * b)   # diminuir porcetagem
    print('-'*30)
    print(f'{"":^5}Resumo do valor')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(num)}') # Com \t você consegue fazer uma tabulação e faz o espaçamento sozinho
    print(f'Dobro do preço: \t{moeda(dobro)}')
    print(f'Metade do preço: \t{moeda(metade)}')
    print(f'80% de aumento: \t{moeda(aumento)}')
    print(f'35% de redução: \t{moeda(reduçao)}')
    print('-'*30)


def moeda(num):
    novo_numero = f'R${num}'
    formatado = novo_numero.replace('.', ',')
    return formatado
