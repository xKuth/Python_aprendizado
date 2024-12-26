palavras = ('aprender', 'programar', 'linguagem', 'curso', 'gratis', 'estudar', 'trabalhar',
            'mercado', 'programar')
vogal = ''
for cont in range(0, len(palavras)):
    print(f'Na palavra {palavras[cont]} temos: ', end=' ')
    contagem_a = palavras[cont].count('a')
    contagem_e = palavras[cont].count('e')
    contagem_i = palavras[cont].count('i')
    contagem_o = palavras[cont].count('o')
    contagem_u = palavras[cont].count('u')
    if 'a' in palavras[cont]:
        vogal += 'a ' * contagem_a
    if 'e' in palavras[cont]:
        vogal += 'e ' * contagem_e
    if 'i' in palavras[cont]:
        vogal += 'i ' * contagem_i
    if 'o' in palavras[cont]:
        vogal += 'o ' * contagem_o
    if 'u' in palavras[cont]:
        vogal += 'u ' * contagem_u
    print(vogal)
    vogal = ''


# Solução do Gustavo Guanabara
'''palavras = ('aprender', 'programar', 'linguagem', 'curso', 'gratis', 'estudar', 'trabalhar',
            'mercado', 'programar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''
