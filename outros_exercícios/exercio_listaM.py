import Vnumeros
cores = {'quebra': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m'}
contagem_num = media = quebra = 0
lista_numeros = []
mudar = ''
dlista = False
while True:
    res = ''
    numero = Vnumeros.verificacao()
    if numero == 0:
        break
    else:
        lista = Vnumeros.cadastro(numero)
        lista_numeros.append(lista[:])
        lista.clear()
    if len(lista_numeros) == 1:
        for cont in range(0, len(lista_numeros[0])):
            contagem_num += lista_numeros[0][cont]
        media = contagem_num / len(lista_numeros[0])
    else:
        contagem_v = 0
        for i, v in enumerate(lista_numeros):
            for cont in v:
                contagem_v += 1
                contagem_num += cont
        media = contagem_num / contagem_v
    contagem_num = 0
    print(f'{cores['verde']}A media da lista digitada foi:{cores['quebra']} {cores['vermelho']}'
          f'{media:.2f}{cores['quebra']}')
    while True:
        try:
            res = str(input(f'{cores['vermelho']}Deseja continuar ?{cores['quebra']} [S/N]: ')).upper()[0]
        except KeyboardInterrupt:
            print(f'{cores['vermelho']}O Usuario preferiu encerrar o programa!{cores['quebra']}')
            quebra = 1
            break
        if res == 'S':
            print('-'*30)
            print('Selecione as opções:')
            print(f'{cores['verde']}1º continuar na mesma lista')
            print(f'{cores['verde']}2º mudar a lista{cores['quebra']}')
            mudar = Vnumeros.numeroverificado()
            if mudar == 1:
                break
            else:
                lista_numeros.clear()
                break
        elif res == 'N':
            break
        else:
            print(f'{cores['vermelho']}O parametro digitado está errado! tente novamente{cores['quebra']}')
    if res == 'N' or quebra == 1:
        break
print(f'{cores['vermelho']}PROGRAMA FINALIZADO!!{cores['quebra']}')
