itens = ('lapis', 'borracha', 'caderno', 'estojo', 'transferidor', 'compasso', 'mochila', 'canetas', 'livro')
preco = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)
print('-'*50)
print(f'{"Listagem de preços":^45}')
print('-'*50)
for cont in range(0, len(itens)):
    print(f'{itens[cont]:.<40}R$ {preco[cont]:>4}')