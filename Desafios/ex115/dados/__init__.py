def fmenu():
    print('-'*30)
    print(f'{"":>7}MENU PRINCIPAL')
    print('-'*30)
    print(f'1 - ver pessoas cadastradas')
    print(f'2 - cadastrar nova pessoa')
    print(f'3 - sair do sistema')
    print('-'*30)
    try:
        opcao = int(input('Sua opção: '))
    except ValueError:
        while True:
            print('o valor digitado não corresponde a valor inteiro')
            opcao2 = str(input('Sua opção: '))
            if opcao2.isnumeric():
                opcao = int(opcao2)
                return opcao
    except KeyboardInterrupt:
        opcao = 3
        print()
        print(f'\033[4;31mO Usuario decidiu encerrar o programa!\033[m')
        return opcao
    while opcao > 3 or opcao < 1:
        print('Erro! digite o valor de (1 a 3)')
        opcao = int(input('Sua opção: '))
    return opcao


def pessoascadastros():
    print('-'*30)
    print(f'{"":>7}PESSOAS CADASTRADAS')
    print('-'*30)
    with open('pessoas.txt', 'r') as arquivo:
        nomes = arquivo.read().strip().split()
    with open('idade.txt', 'r') as arquivo:
        idades = arquivo.read().strip().split()
    for i in range(0, len(nomes)):
        print(f'{nomes[i]:<18}', end='')
        print(idades[i], ' anos')


def novaspessoas():
    nome = ''
    cadastro = {'nome': '', 'idade': 0}
    totcadas = []
    print('-'*30)
    print(f'{"":>7}NOVO CADASTRO')
    print('-'*30)
    try:
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
    except ValueError:
        while True:
            print(f'\033[1;31mDigite um valor inteiro válido\033[m')
            idade2 = str(input('Idade: '))
            if idade2.isnumeric():
                idade = int(idade2)
                break
    except KeyboardInterrupt:
        print()
        print('\033[4;31mo usuario preferiu encerrar o programa\033[m')
        return 3
    cadastro['nome'] = nome
    cadastro['idade'] = idade
    totcadas.append(cadastro.copy())
    cadastro.clear()
    novocadastro(totcadas)
    totcadas.clear()
    print(f'Novo registro de {nome} adicionado')
    return totcadas


def novocadastro(tpessoas):
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'\n{tpessoas[0]["nome"]}')
    with open('idade.txt', 'a') as arquivo:
        arquivo.write(f'\n{tpessoas[0]["idade"]}')


print()
