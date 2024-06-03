import datetime
ano_atual = datetime.date.today().year


def voto(ano):
    idade = ano_atual - ano
    if 16 <= idade < 18 or idade >= 60:
        print(f'Com {idade} anos o voto é opcional')
    elif idade <= 15:
        print(f'Com {idade} anos não vota')
    else:
        print(f'O voto com {idade} anos é obrigatorio')


nasc = int(input('Qual o ano você nasceu? '))
voto(nasc)