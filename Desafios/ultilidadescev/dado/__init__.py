def leiadinheiro(txt):
    ok = False
    valor_retorno = 0
    while True:
        numero = str(input(txt))
        troca = ''
        valor = str(numero)
        if '.' in valor:
            troca = float(numero)
            if float(troca):
                valor_retorno = float(valor)
                ok = True
        if ',' in valor:
            troca = str(numero)
            valor = troca.replace(',', '.')
            troca = float(valor)
            if float(troca):
                valor_retorno = float(valor)
                ok = True
        elif numero.isnumeric():
            print('numererico')
            valor_retorno = int(numero)
            ok = True
        elif valor_retorno != float or int:
            print('Erro! Digite um valor correspondente')
        if ok:
            break
    return valor_retorno

