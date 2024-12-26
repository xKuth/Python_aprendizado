n1 = maior = manor = list()
for cont in range(0, 5):
    n1.append(int(input(f'Digite um valor para a posição {cont}: ')))

print('-='*30)
print(f'Você digitou os valores {n1}')
print(f'O maior valor digitado foi {max(n1)} nas posições ', end='')
for cont in range(0, len(n1)):
    if n1[cont] == max(n1):
        print(f'{cont}...', end=' ')
print(f'\nO menor valor digitado foi {min(n1)} nas posições ', end='')
for cont in range(0, len(n1)):
    if n1[cont] == min(n1):
        print(f'{cont}...', end=' ')