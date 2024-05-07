'''n1 = int(input('Qual o número? '))
if n1 % 2 == 0 and n1 != 2:
    print('Esse não é um \033[1;34mnúmero primo\033[m')
elif n1 % n1 == 0 and n1 % 1 == 0 or n1 == 2:
    print('Esse é um \033[1;34mnúmero primo\033[m')'''

# Solução do Gustavo Guanabara
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divísivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÂO é PRIMO!')
