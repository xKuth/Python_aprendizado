nome_pessoas = []
peso = maior = menor = 0
peso_pessoas = []
registro = 0
while True:
    nome_pessoas.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    if registro == 0:
        maior = peso
        menor = peso
    peso_pessoas.append(peso)
    nome_pessoas.append(peso_pessoas[:])
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    peso_pessoas.clear()
    registro += 1
    res = str(input('Quer continuar ? [S/N] ')).upper()[0]
    if res == 'N':
        break
print(f'Foram cadastradas {(registro)} pessoas')
print(f'A pessoa mais pesada foi {maior} de ', end='')
registro = 0
for cont in range(1, len(nome_pessoas), 2):
    if maior == nome_pessoas[cont][0]:
        registro += 1
        print(end=' e 'if registro > 1 else '')
        print(f'{nome_pessoas[cont-1]}', end='')
print(f'\nA pessoa mais leve foi {menor} de ', end='')
registro = 0
for cont in range(1, len(nome_pessoas), 2):
    if menor == nome_pessoas[cont][0]:
        registro += 1
        print(end=' e 'if registro > 1 else '')
        print(f'{nome_pessoas[cont-1]}',end='')
        registro += 1

