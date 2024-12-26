import math
n1 = float(input('Qual o numero quer analisar? '))
int = math.floor(n1)
print('O número \033[4;32;40m{:.3f}\033[m tem a parte inteira \033[4;32;40m{}\033[m'.format(n1, int))

'''tambem pode ser usar trunc , importando apenas ele mesmo
from math import trunc
print('O valor digitado foi \033[4;32;40m{}\033[m e sua posição inteira é \033[4;32;40m{}\033[m'.format(n1, trunc(int)))'''


'''você tambem pode usar sem importar função com :
num = float(input('Digite um valor '))
print('O valor digitado foi \033[4;32;40m{}\033[m e a sua porção inteira é \033[4;32;40m{}\033[m'.format(num, int(num)))'''
