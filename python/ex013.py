sal = float(input('Qual seu salario? '))
aum = sal * 0.15
novosal = sal + aum
print('Seu salario era \033[1;31m{0}\033[m e vai passar a ser \033[1;36m{1:.2f}\033[m'.format(sal,novosal))