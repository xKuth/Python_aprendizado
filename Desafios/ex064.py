cont = 0
contagem_num = 0
soma = 0
n1 = 0
while cont != 999:
    n1 = int(input('Digite os numeros inteiros: '))
    if n1 != 999:
        contagem_num += 1
        soma = n1 + soma
    elif n1 == 999:
        cont = 999
        print('Finalizando programa!')
print('Foram digitados \033[1;33m{}\033[m números , e a soma entre eles é \033[1;33m{}\033[m'.format(contagem_num, soma))



