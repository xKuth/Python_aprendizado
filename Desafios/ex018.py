import math
an = float(input('Digite um angulo que deseja '))
seno = math.sin(math.radians(an))
print('O angulo de \033[0;31;40m{}\033[m tem o SENO de \033[0;31;40m{:.2f}\033[m'.format(an,seno))
co = math.cos(math.radians(an))
print('O angulo de \033[0;31;40m{}\033[m tem o COSSENO de \033[0;31;40m{:.2f}\033[m'.format(an,co))
tan = math.tan(math.radians(an))
print('O angulo de \033[0;31;40m{}\033[m tem a TANGENTE de \033[0;31;40m{:.2f}\033[m'.format(an,tan))

#Simplificando o codigo importando apenas o necessario
''' 
from math import radians, sin, cos, tan
an = float(input('Digite um angulo que deseja '))
seno = sin(radians(an))
print('O angulo de \033[0;31;40m{}\033[m tem o SENO de \033[0;31;40m{:.2f}\033[m'.format(an,seno))
co = cos(radians(an))
print('O angulo de \033[0;31;40m{}\033[m tem o COSSENO de \033[0;31;40m{:.2f}\033[m'.format(an,co))
tan = tan(radians(an))
print('O angulo de \033[0;31;40m{}\033[m tem a TANGENTE de \033[0;31;40m{:.2f}\033[m'.format(an,tan))'''
