def resumo(num, a, b):
    dobro = num * 2
    metade = num / 2
    aumento = ((num / 100) * a) + num  # aumnetar porcetagem
    reduçao = num - ((num / 100) * b)   # diminuir porcetagem
    print('-'*30)
    print(f'{"":^5}Resumo do valor')
    print('-'*30)
    print(f'Preço analisado: {" ":>2}{moeda(num)}')
    print(f'Dobro do preço: {" ":>3}{moeda(dobro)}')
    print(f'Metade do preço: {" ":>2}{moeda(metade)}')
    print(f'{a}% de aumento: {" ":>3}{moeda(aumento)}')
    print(f'{b}% de redução: {" ":>3}{moeda(reduçao)}')
    print('-'*30)


def moeda(num):
    novo_numero = f'R${num:.2f}'
    formatado = novo_numero.replace('.', ',')
    return formatado
