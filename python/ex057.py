s = ''
while s != 'M' and s != 'F':
    s = str(input('Qual é seu sexo? M/F: ')).upper()
    if s != 'M' and s != 'F':
        print('Digito errado digite novamente')
print('Finalizado')
if s == 'M':
    print('Seu sexo é masculino')
else:
    print('Seu sexo é feminino')

'''# Solução do Gustavo Guanabra
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
'''