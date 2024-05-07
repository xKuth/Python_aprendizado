'''n1 = int(input('Qual é o primeiro termo?  '))
n = int(input('Qual é a razão para o número? '))
soma = n1
for c in range(1, 11):
    print('\033[1;32m',soma,'\033[m', end=',')
    soma = soma + n
print('Finalizado')'''

# solução do Gustavo Guanabara
primeiro = int(input('Primeiro termo '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='♪ ')
print('ACABOU')