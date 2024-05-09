idade = maior = h = m = 0
sexo = cont = ''
fim = 0
while fim < 1:
    sexo = cont = ''
    print('-='*15)
    print('     CADASTRE UMA PESSOA')
    print('-='*15)
    idade = int(input('Idade: '))
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo: [F/M] ')).upper()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    while cont != 'S' and cont != 'N':
      cont = str(input('Quer continuar? [S/N] ')).upper()
    if cont == 'N':
        fim = 2
        break
print('====== FIM DO PROGRAMA ========')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {m} mulheres com menos de 20 anos')




