n = list()
impar = list()
par = list()
res = ''
c = v = 0
while True:
    n.append(int(input('Digite um número: ')))
    res = str(input('Você quer continuar? [S/N] ')).upper()[0]
    if res == 'N':
        break

for cont in range(0, len(n)):
    if n[cont] % 2 == 0:
        par.append(n[cont])
    elif n[cont] % 2 == 1:
        impar.append(n[cont])
print(f'A lista completa é {n}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
