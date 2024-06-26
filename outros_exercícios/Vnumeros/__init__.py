cores = {'quebra': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m'}


def verificacao():
    while True:
        try:
            numero = str(input(f'{cores['verde']}Quantos números você quer a média? {cores['quebra']}'))
            if numero == '0':
                print(f'{cores['vermelho']}0 não é aceito nessa operação!{cores['quebra']}')
            elif numero.isnumeric():
                numero = int(numero)
                return numero
        except (TypeError, ValueError):
            print(f'{cores['vermelho']}Valor digitado não é inteiro ou não é númerico!'
                  f' Tente novamente{cores['quebra']}')
        except KeyboardInterrupt:
            print()
            print(f'{cores['vermelho']}O ÚSUARIO PREFERIU ENCERRAR O PROGRAMA{cores['quebra']}')
            return 0


def cadastro(numero):
    lista = []
    while True:
        print('Quais número deseja adicionar? ')
        for cont in range(0, numero):
            try:
                quant = str(input(f'{cont+1}º: '))
                if quant.isnumeric():
                    quant = int(quant)
                    lista.append(quant)
            except KeyboardInterrupt:
                print(f'{cores['vermelho']}O USUARIO DECIDIU ENCERRAR O PROGRAMA!{cores['quebra']}')
                break
            except (ValueError, TypeError):
                print(f'{cores['vermelho']}valor passado invalido! tente novamente.{cores['quebra']}')
        return lista


def numeroverificado():
    while True:
        try:
            valor = str(input(f'{cores['verde']}digite o valor [1 ou 2]: {cores['quebra']}')).strip()
            if valor.isnumeric() and valor == '1' or valor == '2':
                num = int(valor)
                return num
            else:
                print('Valor não correspondente')
        except (ValueError, TypeError):
            print(f'{cores['vermelho']}O valor verificado não corresponde a inteiro! Tente novamente{cores['quebra']}')
        except KeyboardInterrupt:
            print(f'{cores['vermelho']}O usuario decidiu encerrar o programa!{cores['quebra']}')
            break
