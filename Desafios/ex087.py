matriz = []
auxiliar = []
par = []
soma_coluna3 = []
maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        auxiliar.append(int(input(f'Digite o valor {linha, coluna}:')))
        if auxiliar[coluna] % 2 == 0:
            par.append(auxiliar[coluna])
        if coluna == 2:
            soma_coluna3.append(auxiliar[2])
        if linha == 1 and auxiliar[coluna] > maior:
            maior = auxiliar[coluna]
    matriz.append(auxiliar[:])
    auxiliar.clear()
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^2}]', end=' ')
    print()
print(f'A soma de todos valores pares é {sum(par)}')
print(f'A soma dos valores da 3ª coluna é {sum(soma_coluna3)}')
print(f'O maior valor da segunda linha é {maior}')
