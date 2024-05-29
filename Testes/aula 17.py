'''num = [2, 5, 9, 1]
num[2] = 3 # Adicionando um numero na posição
num.append(7)
num.sort(reverse=True) # Colocando a lista em ordem alfabetica, ou decrecente
num.insert(2, 2) # inserindo número na posição
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número')
# num.pop(2) # excluindo o ultimo número ou o parametro
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''
'''valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''