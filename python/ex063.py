n1 = int(input('Quantos numeros deseja ver de Fibonacci? '))
cont = 0
fibo = 0
soma = 1
auxiliar = 0
while cont < n1:
    print(fibo, end=', ')
    auxiliar = fibo + soma
    soma = fibo
    fibo = auxiliar
    cont += 1

#Solução do Gustavo Guanabara
'''print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} • {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('• {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' • FIM')
print('~'*30)'''