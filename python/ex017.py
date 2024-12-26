import math
cato = float(input('Qual o cateta oposto do triangulo? '))
cata = float(input('Qual o cateto adjacente do triangulo? '))
hipote = math.sqrt((cato**2) + (cata**2))
print('A hipotenusa entre \033[4;35m{}\033[m e \033[4;35m{}\033[m é \033[4;32m{:.2f}\033[mcm'.format(cato,cata,hipote))

'''#ou você pode usar com uma importação para calcular
from math import hypot
co = float(input('Comprimento do cateto oposto '))
ca = float(input('comprimento do cateto adjacente '))
hi = hypot(co,ca)
print('A hipotenusa vai medir \033[4;32m{:.2f}\033[mcm'.format(hi))'''