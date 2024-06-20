def verificação():
    while True:
        try:
            numero = str(input('Quantos números você quer a média? '))
            if numero == '0':
                print('0 não é aceito nessa operação!')
            elif numero.isnumeric():
                numero = int(numero)
                return numero
        except (TypeError, ValueError):
            print('Valor digitado não é inteiro ou não é númerico! Tente novamente')
        except KeyboardInterrupt:
            print()
            print('O ÚSUARIO PREFERIU ENCERRAR O PROGRAMA')
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
                print('O USUARIO DECIDIU ENCERRAR O PROGRAMA!')
                break
            except (ValueError, TypeError):
                print('valor passado invalido! tente novamente.')
        return lista


def numeroverificado():
    while True:
        try:
            valor = str(input('digite o valor [1 ou 2]: ')).strip()
            if valor.isnumeric() and valor == '1' or valor == '2':
                num = int(valor)
                return num
            else:
                print('Valor não correspondente')
        except (ValueError, TypeError):
            print('O valor verificado não corresponde a inteiro! Tente novamente')
        except KeyboardInterrupt:
            print('O usuario decidiu encerrar o programa!')
            break