'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
# galera = [['Joao', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]
# print(galera[2][1])
'''for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(galera)

print(f'Temos {totmai} maior e {totmen} menores de idade')