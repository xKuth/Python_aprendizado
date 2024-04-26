nomecd = str(input('Qual o nome da cidade? '))
nomesepa = nomecd.split()
print('Sua cidade começa com Santo ? {}'.format('Santo' in nomesepa[0]))