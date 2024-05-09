n = 1
mult = 1
cores = {'final': '\033[m', 'verde': '\033[1;32m'}
while n > 0:
    mult = 1
    print('-'*10)
    n = int(input('Digite um número para ver a tabuada: '))
    print('-'*10)
    if n < 0:
        break
    while mult <= 10:
        print(f'{cores['verde']}{n}{cores['final']} X {cores['verde']}{mult} = {n*mult}{cores['final']}')
        mult += 1
print('Programa tabuada finalizada. Volte sempre')
