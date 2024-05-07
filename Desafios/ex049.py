numero = int(input('Insira um número para fazer a multiplicação: '))
mult = 0
print('-='*10)
for c in range(0, 11):
    mult = numero * c
    print('{} x {} = \033[1;34m{}\033[m'.format(c, numero, mult))
print('-='*10)
print('Finalizada!')

'''
#Solução do Gustavo Guanabara
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num , c , num*c))'''
