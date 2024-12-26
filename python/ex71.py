print('='*30)
print('BANCO ELETRÔNICO')
print('='*30)
saque = int(input('Qual valor você quer sacar? '))
dezena_indice = saque // 10 % 10
unidade_indice = saque // 1 % 10
divisao_dezena = (saque / 100)
divisao_completa = divisao_dezena // 1
dezena = (divisao_dezena - divisao_completa) * 100
dezena_dez = 0
while saque > 1:
    if saque > 99:
        dividido_cinq = saque // 50
    if dezena_indice >= 2:
        dividido_vint = int(dezena // 20)
    if dezena_indice == 1:
        dezena_dez = 1
    if dezena_indice % 2 == 1:
        if dezena_indice == 3:
            dezena_dez = int(dezena - 20) // 10
        if dezena_indice == 5:
            dezena_dez = int(dezena - 40) // 10
        if dezena_indice == 7:
            dezena_dez = int(dezena - 60) // 10
        if dezena_indice == 9:
            dezena_dez = int(dezena - 80) // 10
    break
print(f'Total de {dividido_cinq} cédulas de 50R$')
print(f'Total de {dividido_vint} cédulas de 20R$')
print(f'Total de {dezena_dez} cédulas de 10R$')
print(f'Total de {unidade_indice} cédulas de 1R$')
print('='*20)
print('Volte sempre ao Banco Eletrônico, Tenha um bom dia')

# Solução do Gustavo Guanabara
'''print('='*30)
print('{:^30}'.format('Banco Cev'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} células de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao Banco Cev! tenha um bom dia!')'''
