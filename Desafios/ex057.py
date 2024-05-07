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
