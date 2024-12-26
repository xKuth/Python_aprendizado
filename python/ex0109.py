from ex0109 import moeda
preço = float(input('Digite um valor: '))
print('-='*20)
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço)}')
print(f'o dobro de {moeda.moeda(preço)} é {moeda.dobro(preço)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço)}')