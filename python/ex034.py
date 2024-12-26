sal = float(input('Qual é o seu salário? '))

if sal >= 1250:
    salreajustado10 = (sal * 0.10) + sal
    print('Seu salario é \033[1;31m{}\033[m e vai passar a ser \033[1;31m{}\033[m'.format(sal,salreajustado10))
else:
    salreajustado15 = (sal * 0.15) + sal
    print('Seu salário é \033[1;31m{}\033[m e vai passar a ser \033[1;31m{}\033[m'.format(sal, salreajustado15))
