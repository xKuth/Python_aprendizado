'''def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-'*30)


# Programa principal
lin()
print('  Curso em video  ')
lin()
print('  Aprenda Python  ')
lin()
print('  Gustavo guanabara  ')
lin()


titulo('  Curso em video  ')
titulo('  Pytohn é muito bom!  ')
print('Oi')

'''
'''a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)'''

'''def soma(a, b):
    print(f'a = {a} e b = {b}')
    s = a + b
    print(f'A soma A + b = {s}')


# Com rotina programa principal
soma(b=4, a=5) # tambem pode-se usar soma(a=4, b=5) ou ao contrario
soma(7, 2)# você pode deixar sem passar qual parametro vai receber qual, assim o primeiro valor para para o primeiro e o segundo em diante
# Você não pode passar mais que o parametro permite tambem como : soma(3, 9, 5)
# não é possivel apenas usar 1 paramentro quando se tem declarados dois na função.
# è possivel inverter a ordem mas não apenas passar apenas um paramêtro quando a funçao pede dois exemplo : soma(a=4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)
'''
'''def contador(*num): # Passando parametro de varios valores, usado quando não se sabe a quantidade valores
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números ')
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''def dobra(lst): # fazendo dobrar todos valores da lista
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2] # Todos valores passados para função em Python são por referencia e não por valores
dobra(valores)
print(valores)'''

'''def soma(* valores):# usando desempacotamneto em Python para passar varios valores
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)'''