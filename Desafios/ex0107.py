import moeda
preço = float(input('Digite um valor: '))
print('-='*20)
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'o dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando em 10% {preço} temos {moeda.aumentar(preço)}')
print(f'Diminuindo em 13% {preço} temos {moeda.diminuir(preço)}')