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
# Solução dos Gustavo Guanabara
'''while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')'''