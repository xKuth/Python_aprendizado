for c in range(1, 51):
    if c % 2 == 0:
        print('\033[1;32m',c,'\033[m')
print('\033[4mContagem finalizada\033[m')

'''
# resolução do Gustavo Guanabara

for n in range(2, 51, 2): #Melhor forma de economizar processador
    print(n, end=' ')
print('ACABOU')'''
