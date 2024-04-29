v = float(input('Quantos reais você tem disponivel para comprar? '))
d = v / 5.10
print('Você possui {0} e pode comprar US$\033[1;31m{1:.2f}\033[m doláres.'.format(v,d))