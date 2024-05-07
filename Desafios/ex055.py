maispesado = 0
maisleve = 100
for c in range(0, 5):
    peso = float(input('Qual é seu peso? '))
    if peso > maispesado:
        maispesado = peso
    if peso < maisleve:
        maisleve = peso
print('A pessoa mais pesada tem {}, e a mais leve tem {}'.format(maispesado, maisleve))

'''# Solução do Gustavo Guanbara
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}• pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
'''