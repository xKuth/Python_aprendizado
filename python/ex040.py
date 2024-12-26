'''nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
m = (nota1 + nota2) /2
if m <= 5:
    print('Sua nota foi {} \033[4;31;40m REPROVADO \033[m'.format(m))
elif (m > 5) and (m < 6.9):
    print('Sua nota foi {} \033[4;36;40m RECUPERAÇÃO \033[m'.format(m))
else:
    print('Sua nota foi {} \033[4;34;40m APROVADO \033[m'.format(m))'''

#soluçao Gustavo Guanabara
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Trirando {:.1f} e {:.1f}, a media de aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está em recuperação.')
elif media < 5:
    print('O aluno esta Reprovado.')
elif media >= 7:
    print('o aluno está Aprovado')
