itens = ('lapis', 'borracha', 'caderno', 'estojo', 'transferidor', 'compasso', 'mochila', 'canetas', 'livro')
preco = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)
print('-'*50)
print(f'{"Listagem de preços":^45}')
print('-'*50)
for cont in range(0, len(itens)):
    print(f'{itens[cont]:.<40}R$ {preco[cont]:>4}')

'''listagem = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
            'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)'''
