num = int(input('Qual o número deseja calcular? '))
d = num * 2
trip = num * 3
raiz = num ** 0.5
cor = {'azul': '\033[1;34m', 'limpa': '\033[m'}
print('O numero é {4}{0}{5} \n seu dobro é {4}{1}{5} \n seu triplo é {4}{2}{5} \n e sua raiz quadrada é {4}{3:.2f}{5}'.format(num,d,trip,raiz,cor['azul'],cor['limpa']))
#Outra maneira de fazer
#print('O numero é {0} \n seu dobro é {1} \n seu triplo é {2} \n e sua raiz quadrada é {3:.2f}'.format(num,(num*2),(num*3),(num**(1/2) ou pow(num,(1/2)))
