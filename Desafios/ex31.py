kmcobrado = int(input('Quantos km você vai viajar? '))
if kmcobrado <= 200:
    valor = kmcobrado * 0.50
    print('Seu km é abaixo de 200 ,o valor a ser pago é de \033[0;35m{}\033[m'.format(valor))
else:
    valor2 = kmcobrado * 0.45
    print('Seu km é acima de 200 ,o valor a ser pago é de \033[0;35m{}\033[m'.format(valor2))
