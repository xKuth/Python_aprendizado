import random
#ou usar apenas importação que vai usar (from random import shuffle)

aluno1 = input('nome do Primeiro aluno? ')
aluno2 = input('nome do Segundo aluno ? ')
aluno3 = input('nome do Terceiro aluno? ')
aluno4 = input('nome do Quarto aluno ? ')
decks = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(decks)
print('A ordem de apresentação será ')
print(decks)
