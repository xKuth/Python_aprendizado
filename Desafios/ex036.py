casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
anos = float(input('Em quantos anos você vai pagar? '))
parcelacasa = (casa / 12) / anos
porcentsal = sal * 0.30

if parcelacasa > porcentsal:
    print('Empréstimo negado')
    print('Seu salário é imcompativel com a quantidade de parcelas a ser paga!')
    print('As parcelas seriam \033[4;31m{:.2f}\033[m por mês'.format(parcelacasa))
elif porcentsal >= parcelacasa:
    print('Empréstimo aprovado:\nVocê pode financiar sua casa!!!')
    print('você vai pagar R$\033[4;31m{:.2f}\033[m por mês'.format(parcelacasa))

#solução do Gustavo Guanabara
'''casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} ano'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Empréstino NEGADO!')'''