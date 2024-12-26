nome = str(input('Qual nome deseja verificar? '))
nomesepa = nome.split()
nomejun = ''.join(nomesepa).upper()
print('Seu nome possui Silva? \033[1;31;40m{}\033[m'.format('SILVA' in nomejun))

#Solução do Gustavo Guanabara

'''nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? \033[1;31;40m{}\033[m'.format('SILVA' in nome.upper()))'''
