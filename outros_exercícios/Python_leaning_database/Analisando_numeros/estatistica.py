cont = 0
with open('numeros_sorteados.txt', 'r') as numeros:
    valores = numeros.read()
    r = valores.split()
    nova_lista = r
    for i in range(0, 10):
        mais_aparicao = max(r, key=r.count)
        cont += 1
        print(cont, 'º numero:', '\033[4;31;40m', mais_aparicao, '\033[m')

        for element in nova_lista:
            if element == mais_aparicao:
                r.remove(mais_aparicao)

'''
apar = 0
    for i, elem in enumerate(r):
        valor = elem
        cont_num = 0
        for indice in range(len(r)):
            if valor == r[indice]:
                cont_num += 1
            if cont_num > apar:
                apar = cont_num
                alt = valor
                if r[-1]:
                    print(apar, alt)
'''


