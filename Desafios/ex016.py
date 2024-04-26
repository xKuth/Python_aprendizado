import math
n1 = float(input('Qual o numero quer analisar? '))
int = math.floor(n1)
print('O número {:.3f} tem a parte inteira {}'.format(n1, int))

'''tambem pode ser usar trunc , importando apenas ele mesmo
from math import trunc
print('O valor digitado foi {} e sua posição inteira é {}'.format(n1, trunc(int)))'''


'''você tambem pode usar sem importar função com :
num = float(input('Digite um valor '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''
