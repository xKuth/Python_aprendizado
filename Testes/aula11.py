'''a = 3
b = 5
print('Os valores são \033[32m{}\033[m e ○ \033[31m{}\033[m '.format(a, b))'''

'''nome = 'Guanabara'
print('Óla! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m' ,nome, '\033[m'))'''

nome = 'Guanabara'
cores = {'limpa': '\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretobranco': '\033[7;30m'}

print('Óla! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretobranco'], nome, cores['limpa']))