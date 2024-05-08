res = ''
soma = 0
cont = 0
maior = 0
menor = 0
while res != 'N':
    print('-='*15)
    n1 = int(input('Digite os números inteiros: '))
    if cont == 0:
        maior = n1
        menor = n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    res = str(input('Você continuar? [S/N] ')).upper()
    soma = n1 + soma
    cont += 1
media = soma / cont
print('A média entre todos valores digitados são {}'.format(media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
