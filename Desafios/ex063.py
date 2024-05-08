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
