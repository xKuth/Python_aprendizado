pessoas = {}
cadastro = []
mulheres = []
soma = 0
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo: [F/M] ')).upper()[0]
    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas.copy()['Nome'])
    pessoas['Idade'] = int(input('idade: '))
    soma += pessoas['Idade']
    res = str(input('Quer continuar ? [S/N] ')).upper()[0]
    cadastro.append(pessoas.copy())
    pessoas.clear()
    if res == 'N':
        break
media = soma / len(cadastro)
print('='*30)
print(f'O total de pessoas cadastras foram {len(cadastro)}')
print(f'A média de idade das pessoas cadastradas foram {media:.2f}')
print(f'As mulheres cadastradas foram ', end='')
contador = len(mulheres)

for cont in mulheres:
    contador -= 1
    print(f'{cont} ', end='e 'if contador != 0 else ' ')

print('\nAs pessoas acima da media foram: ', end=' ')

contador = len(cadastro)

for cont in range(0, len(cadastro)):
    contador -= 1
    if cadastro[cont]['Idade'] > media:
        print(f'{cadastro[cont]['Nome']} ', end='e ' if contador != 0 else '')



# Solução do Gustavo Guanabara
'''galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M e F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'a) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k,v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<< ENCERRADO >>')
'''