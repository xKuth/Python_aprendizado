nome = str(input('Qual seu nome completo? '))
print('Seu nome completo é {}'.format(nome))
nomesepa = nome.split()
nomecontra = nomesepa[::-1]
print('Seu primeiro nome é \033[1;31m{}\033[m'.format(nomesepa[0]))
print('Seu ultimo nome é \033[1;31m{}\033[m'.format(nomecontra[0]))

#Solução dos Gustavo guanabara
'''n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é \033[1;31m{}\033[m'.format(nome[0]))
print('Seu Último nome é \033[1;31m{}\033[m'.format(nome[len(nome)-1]))'''
