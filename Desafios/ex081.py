n = list()
valor = ''
while True:
    n.append(int(input('Digite um número: ')))
    res = str(input('Você quer continuar ? [S/N] ')).upper()[0]
    if 5 in n:
        valor = 'Faz parte da lista'
    else:
        valor = 'Não faz parte da lista'
    if res == 'N':
        break
n.sort(reverse=True)
print(f'O total de números de números digitados foram {len(n)}')
print(f'A lista digitada em forma de ordem decrecente é {n}')
print(f'O valor 5 {valor}')

# Solução do Gustavo Guanabara
'''valores = []
while True:
    valores.append(int(input('Digite um valor :')))
    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrecente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista!')'''