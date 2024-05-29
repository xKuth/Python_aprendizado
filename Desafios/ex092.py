import datetime
total = []
ano = datetime.date.today().year
while True:
    cadastro1 = {'nome': str(input('Nome: ')), 'nascimento': int(input('Ano de nascimento '))}
    cadastro1['idade'] = ano - cadastro1['nascimento']
    cadastro1['Ctps'] = int(input('Carteira de trabalho (0 não tem) '))
    del cadastro1['nascimento']
    break
if cadastro1['Ctps'] == 0:
    print('-=' * 15)
    print(cadastro1)
    for i, v in cadastro1.items():
        print(f'O {i} tem valor {cadastro1[i]}')
elif cadastro1['Ctps'] != 0:
    cadastro1['contrataçao'] = int(input('Ano de contratação '))
    cadastro1['salario'] = float(input('Sálario R$ '))
    cadastro1['aposentadoria'] = (35 - (ano - cadastro1['contrataçao'])) + cadastro1['idade']
    print('-='*15)
    for i, v in cadastro1.items():
        print(f'O {i} tem o valor {cadastro1[i]}')

# Solução do Gustavo Guanabara
'''from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome '))
nasc = int(input('Ano de nascimento '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho ? (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['sálario'] = float(input('Sálario R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  -{k} tem valor {v}')
'''

