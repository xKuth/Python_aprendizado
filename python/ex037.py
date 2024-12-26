num = int(input('Qual nùmero deseja analisar? '))
n1 = int(input('Digite um número para conversão:\n-1 para Binário:\n-2 para octal:\n-3 para hexadecimal:\n'))

if n1 == 1:
    print('\033[1;33;40m',bin(num)[2:],'\033[m')
elif n1 == 2:
    print('\033[1;33;40m',oct(num)[2:],'\033[m')
elif n1 == 3:
    print('\033[1;33;40m',hex(num)[2:],'\033[m')
else:
    print('Erro Digite o número correspondente')
