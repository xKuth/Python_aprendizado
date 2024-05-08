n1 = float(input('Digite um número: '))
mult = n1 - 1
fatorial = n1 * mult
while mult != 1:
    mult = mult - 1
    fatorial = fatorial * mult
print('o fatorial de !{} é {:.1f}'.format(n1, fatorial))
