nomecd = str(input('Qual o nome da cidade? '))
nomesepa = nomecd.split()
print('Sua cidade começa com Santo ? \033[0;34m{}'.format('Santo' in nomesepa[0]), '\033[m')

#solução do Gustavo Guanabra
'''cid = str(input('Em que cidade você nasceu? ')).strip()
print('\033[0;34m', cid[:5].upper() == 'SANTO', '\033[m')'''