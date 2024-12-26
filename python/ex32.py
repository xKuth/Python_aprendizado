ano = int(input('Qual ano deseja analisar? '))
anocent = ano / 100
anodeci = ano // 10 % 10
anouni = ano // 1 % 10
soma = anodeci + anouni

if (ano % 4 == 0) and (soma != 0):
    print('O ano é \033[1;33mBisexto\033[m')
elif anocent % 4 == 0:
    print('O ano é \033[1;33mBisexto\033[m')
else:
    print('O ano não é \033[1;33mBisexto\033[m')

#Solução do Gustavo Guanabara
'''from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1;33m{}\033[m é \033[1;33mBisexto\033[m'.format(ano))
else:
    print('O ano \033[1;33m{}\033[m não é \033[1;33mBisexto\033[m'.format(ano))'''


