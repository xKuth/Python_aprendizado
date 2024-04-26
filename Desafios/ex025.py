nome = str(input('Qual nome deseja verificar? '))
nomesepa = nome.split()
nomejun = ''.join(nomesepa).upper()
print('Seu nome possui Silva? {}'.format('SILVA' in nomejun))
