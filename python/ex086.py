matriz = []
auxiliar= []
for coluna in range(0, 3):
    for linha in range(0, 3):
        auxiliar.append(int(input(f'Digite um valor para {[coluna, linha]}: ')))
    matriz.append(auxiliar[:])
    auxiliar.clear()
print('-='*15)
for coluna in range(0, 3):
    for linha in range(0, 3):
        print(f'[ {matriz[coluna][linha]:^2}]', end=' ')
    print()
