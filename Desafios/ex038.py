n1 = int(input('Qual o primeiro número deseja comparar? '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro valor \033[0;33m{}\033[m é maior'.format(n1))
elif n2 > n1:
    print('O segundo valor \033[0;33m{}\033[m é maior'.format(n2))
else:
    print('Os números \033[0;33m{}\033[0;33m e \033[0;33m{}\033[m são iguais'.format(n1,n2))
