temp = float(input('Informe a temperatura em *C: '))
conversor = (temp * 1.8) + 32
print('A temperatura de \033[4;33m{}\033[m*C corresponde a \033[4;33m{:.2f}\033[m*F!'.format(temp,conversor))
