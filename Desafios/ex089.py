nomes = []
nota = []
media = []
completo = []
contador = 1
contador_nomes = contagem = 0
while True:
    nomes.append(str(input('Nome: ')))# Add o nomes na lista
    contador_nomes += 1
    nota.append(float(input(f'{contador}ª Nota: ')))# Add as notas dentro da lista
    nota.append(float(input(f'{contador}ª nota: ')))
    media.append((nota[0] + nota[1]) / 2)
    nomes.append(nota[:])# Add as notas dentro do indice nome
    nomes.append(media[:])# Add a media no proximo índice dentro de nome
    completo.insert(contagem, nomes[:])# Add a lista completa dentro de outra lista
    nota.clear()
    media.clear()
    nomes.clear()
    contador = 1
    contagem += 1
    res = str(input('Quer continuar? [S/N] ')).upper()[0]
    if res == 'N':
        break
print('-='*15)
print(f'{'No.':>2} {'nome':<20}{'MÉDIA'}')
print('='*30)
for cont in range(0, len(completo)): # Fazendo a matriz com nomes e suas medias
    print(f'{cont:<4}\033[1;32m{completo[cont][0]:<20}\033[m', end='')
    print(f'\033[4;31m{completo[cont][2]}\033[m')
    contador += 1
print('-='*15)
while True:
    res = int(input('Mostrar nota de qual aluno? (999 interrompe) ')) # Pergunta se quer ver as notas digitadas
    if res == 999:
        break
    print(f'Notas de \033[1;32m{completo[res][0]}\033[m são \033[1;31m{completo[res][1]}\033[m')
    print('='*15)
print('FINALIZANDO')
print('<----VOLTE SEMPRE---->')


# Solução do Gustavo Guanabara
'''ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('nota 2: '))
    media= (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')'''