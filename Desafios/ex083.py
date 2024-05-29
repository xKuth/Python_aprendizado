cont = 0
expressao = str(input('Digite a expressão: '))
for p in expressao:
    for letra in p:
        if '('in letra:
            cont += 1
        if ')' in letra:
            cont += 1
if cont % 2 == 0:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta errada!')

# Solução do Gustavo Guanabara
'''expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')'''