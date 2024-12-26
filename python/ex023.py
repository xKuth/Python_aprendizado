'''num = str(input('Qual o numero deseja verificar? '))
print('Unidade:\033[1;31;40m{}\033[m'.format(num[3]))
print('Dezena:\033[1;31;40m{}\033[m'.format(num[2]))
print('Centena:\033[1;31;40m{}\033[m'.format(num[1]))
print('Milhar:\033[1;31;40m{}\033[m'.format(num[0]))'''

#Solução dos Gustavo Guanabara
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: \033[1;31;40m{}\033[m'.format(u))
print('Dezena: \033[1;31;40m{}\033[m'.format(d))
print('Centena: \033[1;31;40m{}\033[m'.format(c))
print('Milhar: \033[1;31;40m{}\033[m'.format(m))