soma = 0
cont = 0
for c in range(1, 500):
    if (c % 3 == 0) and (c % 2 == 1):
        cont = cont + 1
        soma += c
print('O Valor da soma de todos numeros impares de 1 a 500 e multiplos de 3 é \033[1;31m{}\033[m e são \033[1;31m{}\033[m numeros'.format(soma, cont))
print('Finalizado')

'''# Solução do Gustavo Guanabra
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))'''
