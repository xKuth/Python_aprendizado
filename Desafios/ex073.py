tabela = ('Athletico- PR', 'Bahia', 'Flamengo', 'Botafogo', 'Cruzeiro', 'Atlético-MG', 'Braganta',
          'Palmeiras', 'São paulo', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco da gama', 'Cricíuma', 'Juventude',
          'Corinthians', 'Fluminense', 'Ec Vitória', 'Atlético-GO', 'Cuiabá')
print('=-'*50)
print(f'Lista de times de Brasileirão: {tabela}')
print('=-'*50)
print('Os 5 primeiros são: ', end='')
for cont in range(0, 5):
    print(tabela[cont], end=', 'if cont < 4 else '\n')
print('=-'*50)
print('Os 4 primeiros são: ', end='')
for cont in range(16, 20):
    print(tabela[cont], end=', ' if cont < 19 else '\n')
print('=-'*50)
print('Times em ordem alfabética: {}'.format(sorted(tabela)))
print('=-'*59)
print('O Cruzeiro está na {} posição'.format(tabela.index('Cruzeiro')+1))

# Solução do Gustavo Guanabara
'''times = ('Athletico- PR', 'Bahia', 'Flamengo', 'Botafogo', 'Cruzeiro', 'Atlético-MG', 'Braganta',
          'Palmeiras', 'São paulo', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco da gama', 'Cricíuma', 'Juventude',
          'Corinthians', 'Fluminense', 'Ec Vitória', 'Atlético-GO', 'Cuiabá')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Cruzeiro está na {times.index('Cruzeiro')+1}° posição')'''