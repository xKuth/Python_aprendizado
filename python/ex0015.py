alug = int(input('Quantos dias alugados? '))
alugkm = float(input('Quantos Km rodados? '))
odia = alug * 60
okm = alugkm * 0.15
t = odia + okm
print('O total a pagar é de \033[1;31;40m{0}\033[m'.format(t))