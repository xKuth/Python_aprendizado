def resumo(num, a, b):
    dobro = num * 2
    metade = num / 2
    aumento = ((num / 100) * a) + num  # aumnetar porcetagem
    reduçao = num - ((num / 100) * b)   # diminuir porcetagem
    print('-'*30)
    print(f'{"":^5}Resumo do valor')
    print('-'*30)
    print(f'Preço analisado: {moeda(num):>3}')
    print(f'Dobro do preço: {moeda(dobro):>9}')
    print(f'Metade do preço: {moeda(metade):>3}')
    print(f'80% de aumento: {moeda(aumento):>8}')
    print(f'35% de redução: {moeda(reduçao):>8}')
    print('-'*30)


def moeda(num):
    novo_numero = f'R${num}'
    formatado = novo_numero.replace('.', ',')
    return formatado
