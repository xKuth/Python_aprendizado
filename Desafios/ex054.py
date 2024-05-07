from datetime import date
maior = 0
menor = 0
ano = date.today().year
for c in range(0, 7):
    nome = int(input('Qual ano você nasceu? '))
    idade = ano - nome
    if idade <= 17:
        menor = menor + 1
    else:
        maior = maior + 1
print('De todas pessoas ,{} sao de maiores e {} são de menores'.format(maior, menor))