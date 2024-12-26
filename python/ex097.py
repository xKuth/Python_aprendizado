

def escreva(txt):
    for cont in range(0, len(txt)):
        print('-', end='')
    print()
    print(txt)
    for cont in range(0, len(txt)):
        print('-', end='')
    print()


escreva('  Gustavo guanabara  ')
escreva('  Curso de python no Youtube  ')
escreva('  CEV  ')


# Solução do Gustavo Guanabara
'''def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
escreva('Gustavo Gunabara')
escreva('Curso de Python no Youtube')
escreva('Cev')'''
