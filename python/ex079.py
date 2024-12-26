n1 = list()
cont = add = 0
while True:
    res = ''
    add = int(input('Digite um valor: '))
    if add not in n1:
        n1.append(add)
        print('Valor adicionado com sucesso...')
    elif add in n1:
        print('Valor duplicado! Não vou adicionar...')
    res = str(input('Quer continuar ? [S/N] ')).upper()[0]
    if res == 'N':
        break
    cont += 1
n1.sort()
print('-='*15)
print(f'Você digitou os valores {n1}')
