import math
cato = float(input('Qual o cateta oposto do triangulo? '))
cata = float(input('Qual o cateto adjacente do triangulo? '))
hipote = math.sqrt((cato**2) + (cata**2))
print('A hipotenusa entre {} e {} é {:.2f}cm'.format(cato,cata,hipote))

'''#ou você pode usar com uma importação para calcular
from math import hypot
co = float(input('Comprimento do cateto oposto '))
ca = float(input('comprimento do cateto adjacente '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}cm'.format(hi))'''