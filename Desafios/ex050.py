soma = 0
for c in range(1, 7):
    n1 = int(input('Qual o primeiro {}•valor: '.format(c)))
    if n1 % 2 == 0:
        soma = n1 + soma
print('A soma dos números digitados foi \033[1;44;40m{}\033[m'.format(soma))

'''#Solução do Gustavo Guanabara
soma = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor '.format(c)))
    if num % 2 == 0:
        soma += num
        count += 1
print('Você informou {} números PARES e a soma foi {}'.format(count, soma))
'''