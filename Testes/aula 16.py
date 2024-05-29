lanche = ( 'Hmaburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# Tuplas são imutaveis
'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posiçaõ {pos}')
'''

# print(sorted(lanche)) # não muda a string, so coloca em ordem.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) # contar quantas vezes aparace um número
print(c.index(4)) # ver qual a posição do número
pessoa = ('Gustavo', 39, 'M', 99.88) # Você pode colocar tanto string quanto núemros em uma tupla
# del(pessoa) # As duplas são imutaveis mas é possivel apagar uma, com dell
# del(pessoa[0]) # não é possivel apagar elementos dentro da tupla
print(pessoa)
