import random

aluno1 = input('Nome do primeiro aluno? ')
aluno2 = input('Nome do segundo aluno? ')
aluno3 = input('Nome do terceiro aluno? ')
aluno4 = input('Nome do quarto aluno? ')
print(random.choice([aluno1, aluno2, aluno3, aluno4]))

#Ou você pode fazer uma lista e importar so elementos necessarios
'''from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''

