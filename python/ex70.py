print('-='*15)
print('      LOJA TUDO BARATO')
print('-='*15)
prod_final = False
s =  contador = preco = preco_menor = preco_mil = 0
prod = cont = mais_barato = ''
while not prod_final:
    cont = ''
    prod = str(input('Nome do produto: '))
    preco = float(input('preço: '))
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()
    contador += 1
    s += preco
    if contador == 1:
        preco_menor = preco
        mais_barato = prod
    if preco < preco_menor:
        preco_menor = preco
        mais_barato = prod
    if preco >= 1000:
        preco_mil += 1
    elif cont in 'N'[0]:
        break
print(f'O total gasto na compra foi {s}')
print(f'O total de produto acima de R$1000 é {preco_mil}')
print(f'O nome do produto mais barato é {mais_barato} e o valor é R${preco_menor}')