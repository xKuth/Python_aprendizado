lista = list()
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0:
        lista.append(n)
        maior = menor = n
        print('Adicionando ao final da lista...')
    elif n <= min(lista):
        lista.insert(0, n)
        print(f'Adicionando na posição {lista.index(n)} da lista...')
    elif n >= max(lista):
        lista.append(n)
        print('Adicionando ao final da lista...')
    elif n > min(lista):
        lista.insert(1, n)
        print(f'Adicionando na posição {lista.index(n)} da lista...')
print('=-'*15)
print(f'Os valores digitados em ordem formam {lista}')

# Solução do Gustavo Guanabara
'''lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')'''