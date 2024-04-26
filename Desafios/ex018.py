import math
an = float(input('Digite um angulo que deseja '))
seno = math.sin(math.radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an,seno))
co = math.cos(math.radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an,co))
tan = math.tan(math.radians(an))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(an,tan))

#Simplificando o codigo importando apenas o necessario
''' 
from math import radians, sin, cos, tan
an = float(input('Digite um angulo que deseja '))
seno = sin(radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an,seno))
co = cos(radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an,co))
tan = tan(radians(an))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(an,tan))'''
