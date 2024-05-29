nome = {'Nome': str(input('nome: '))}
nome['Média'] = float(input(f'media de {nome['Nome']}: '))
print(f'O nome é igual a {nome["Nome"]} ')
print(f'Média é igual a {nome["Média"]:.1f}')
if nome['Média'] >= 7:
    print('Situação é igual a Aprovado')
elif 5 <= nome["media"] <= 7:
    print('Situação é igual a recuperação')
else:
    print('A situação é igual a reprovado')

# Solução do Gustavo Guanabara
'''aluno = dict()
aluno['nome'] = str(input('nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno["media"] >= 7:
    aluno["situação"] = 'Aprovado'
elif 5 <= aluno['media'] <= 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'  -{k} é igual a {v}')'''