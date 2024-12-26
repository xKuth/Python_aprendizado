nome = str(input('Digite um nome: '))
print('\033[1;34m',nome.upper(),'\033[m')
print('\033[1;34m',nome.lower(),'\033[m')
nomesepa = nome.split()
nomejun = ''.join(nomesepa)
print('Seu nome possuí \033[1;34m{}\033[m carcateres'.format(len(nomejun)))
print('Seu primeiro nome tem \033[1;34m{}\033[m caracteres'.format(len(nomesepa[0])))

#Solução do Gustavo Guanabara

'''
nome = str(input('Digite seu nome completo ')).strip()
print('Analisando seu nome ')
print('Seu nome em Miusculas é \033[1;34m{}\033[m'.format(nome.upper()))
print('Seu nome em Minusculas é \033[1;34m{}\033[m'.format(nome.lower()))
print('Seu nome tem ao todo \033[1;34m{}\033[m letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem \033[1;34m{}\033[m letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é \033[1;34m{}\033[m e ele tem \033[1;34m{}\033[m letras'.format(separa[0], len(separa[0])))'''
