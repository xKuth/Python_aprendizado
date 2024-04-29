n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#Verificar maior número:

if (n1 > n2) and (n1 > n3):
    print('O maior numero é \033[0;32;40m{}\033[m'.format(n1))
elif (n2 > n1) and (n2 > n3):
    print('O maior número é \033[0;32;40m{}\033[m'.format(n2))
else:
    print('O maior número é \033[0;32;40m{}\033[m'.format(n3))

#Verificar menor número:

if (n1 < n2) and (n1 < n3):
    print('O menor numero é \033[0;32;40m{}\033[m'.format(n1))
elif (n2 < n1) and (n2 < n3):
    print('O menor número é \033[0;32;40m{}\033[m'.format(n2))
else:
    print('O menor numero é \033[0;32;40m{}\033[m'.format(n3))

#Solução Gustavo Guanabara
'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi \033[0;32;40m{}\033[m'.format(menor))
print('O maior valor digitado foi \033[0;32;40m{}\033[m'.format(maior))'''

