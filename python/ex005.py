n1 = int(input('Qual numero deseja verificar? '))
post = n1 + 1
ant = n1 - 1
cor = {'verde': '\033[1;32m', 'limpa': '\033[m'}
print('O numero é {0}{1}{4} seu anterior é {0}{2}{4} e seu sucessor é {0}{3}{4}'.format(cor['verde'],n1,ant,post,cor['limpa']))
