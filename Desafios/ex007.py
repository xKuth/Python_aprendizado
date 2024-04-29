nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
m = (nota1 + nota2)/2
print('A media dos alunos é \033[4;31m{:.1f}\033[m'.format(m))