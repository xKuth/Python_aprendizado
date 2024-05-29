'''pessoas = {'nome': 'gustavo', 'Sexo': 'M', 'Idade': 22}
# print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos.')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# del pessoas['Sexo']
# pessoas['nome'] = 'leandro'
# pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
'''Brasil = []
estado = {'uf': 'rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'são paulo', 'sigla': 'SP'}
Brasil.append(estado)
Brasil.append(estado2)
print(Brasil[1]['sigla'])
'''
'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federadiva: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()'''
