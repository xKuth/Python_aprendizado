n1 = float(input('Digite um número para calcular o fatorial: '))
mult = n1 - 1
fatorial = n1 * mult
while mult != 1:
    mult = mult - 1
    fatorial = fatorial * mult
print('o fatorial de !{} é {:.1f}'.format(n1, fatorial))

# com estrutura FOR:
'''n1 = int(input('Digite um fatorial: '))
valor = n1
fatorial = n1
print('O fatorial de {}! é: {} x'.format(n1, valor), end=' ')
for c in range(n1, 1, -1):
    valor = valor - 1
    mult = fatorial * valor
    fatorial = mult
    print('{}'.format(valor), end='')
    print(' x ' if valor > 1 else ' = ', end='')
print(fatorial)'''



#Solução do Gustavo Guanabara
'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''