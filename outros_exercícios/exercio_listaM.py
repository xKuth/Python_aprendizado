import Vnumeros
contagem_num = media = quebra = 0
lista_numeros = []
mudar = ''
dlista = False
while True:
    res = ''
    numero = Vnumeros.verificação()
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
    print(f'A media da lista digitada foi: {media:.2f}')
    while True:
        try:
            res = str(input('Deseja continuar ? [S/N]: ')).upper()[0]
        except KeyboardInterrupt:
            print('O Usuario preferiu encerrar o programa!')
            quebra = 1
            break
        if res == 'S':
            print('-'*30)
            print('Selecione as opções:')
            print('1º continuar na mesma lista')
            print('2º mudar a lista')
            mudar = Vnumeros.numeroverificado()
            if mudar == 1:
                break
            else:
                lista_numeros.clear()
                break
        elif res == 'N':
            break
        else:
            print('O parametro digitado está errado! tente novamente')
    if res == 'N' or quebra == 1:
        break
print('PROGRAMA FINALIZADO!!')
