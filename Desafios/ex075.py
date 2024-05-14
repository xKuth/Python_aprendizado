par = str()
contador = contador_tres = 0
n1 = str(input('Digite um número: '))
n2 = str(input('Digite outro número: '))
n3 = str(input('Digite mais um número: '))
n4 = str(input('Digite o último número: '))
final = (n1 + n2 + n3 + n4)
print(f'Você digitou os valores ', end=' ')
for cont in range(0, 4):
    print(final[cont], end=' 'if cont < 3 else '\n')
    if final[cont] == '9':
        contador += 1
    if final[cont] == '3':
        contador_tres += 1
    if int(final[cont]) % 2 == 0:
        par += final[cont]

print('O valor 9 foi digitado {} vezes'.format(contador))
if contador_tres > 0:
    print('O valor 3 apareceu na {} posição'.format(final.index('3')))
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares foram ', end='')
for cont in range(0, len(par)):
    print(par[cont], end=' ' if cont > 0 else ' ')

