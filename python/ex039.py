from datetime import date
nascimento = int(input('Qual ano você nasceu? '))
ano = date.today().year
idade = ano - nascimento
selecao = int(input('Você é homem ou mulher ?\n 1-homem:\n 2-Mulher:\n '))
if selecao == 2:
    print('Como você é mulher não precisa se alistar')
else:
    print('Sua idade é {}'.format(idade))
if (idade < 18) and (selecao != 2):
    falta_alistamento = 18 - idade
    print('Você precisa se alistar no exercíto daqui \033[4;31m{}\033[m anos'.format(falta_alistamento))
elif (idade > 18) and (selecao != 2):
    tempo_alistamento = idade - 18
    print('Ja passou do tempo de alistamento!!')
    print('O prazo de alistamento ja passou \033[4;31m{}\033[m anos'.format(tempo_alistamento))
elif (selecao != 2):
    print('Você precisa de alistar no exercito esse ano!!!')