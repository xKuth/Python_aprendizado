pares_impar = []
n1 = 0
auxiliar_par = []
auxiliar_impar = []
for cont in range(0, 7):
    n1 = int(input(f'Digite o {cont}ª número: '))
    if n1 % 2 == 0:
        auxiliar_par.append(n1)
    elif n1 % 2 == 1:
        auxiliar_impar.append(n1)
auxiliar_par.sort()
auxiliar_impar.sort()
pares_impar.append(auxiliar_par[:])
pares_impar.append(auxiliar_impar[:])
print('-='*30)
print(f'Os valores pares digitados foram {pares_impar[0]}')
print(f'Os valores impares digitados foram {pares_impar[1]}')
# Solução do Gustavo guanabara
'''num = [[], []]
valor = 0
for c in range(0, 8):
    valor = int(input(f'Digite o {c}*. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
'''

