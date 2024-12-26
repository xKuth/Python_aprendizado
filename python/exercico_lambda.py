'''# script anonima.py (versão alterada do script funcao5.py)
def multiplicar_por(multiplicador):
        lambda multiplicando: multiplicando * multiplicador

def main():
    multiplicar_por_10 = multiplicar_por(10)
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))
 
    multiplicar_por_5 = multiplicar_por(5)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))

if __name__ == "__main__":
    main()
'''
'''
#  Colocando todas letras em maiusculas com programação funcional
veiculos = ['aviao', 'carro', 'navio', 'onibus']

tot_elementos = lambda x: str.upper(x)
nomes_maiusculas = list(map(tot_elementos, veiculos))
print(f'nomes maisculos: {nomes_maiusculas}')

# Encontrando valores pares com programação funcional
lista = [0,1,1,2,3,5,8,13,21,34]
pares = lambda p: p % 2 == 0
print(f'teste de paridade(5) = {pares(5)}')
lista_pares = list(filter(pares, lista))
print(f'lista de números pares: {lista_pares}')'''

'''# diminuindo casas decimais com duas lista e programação funcional
lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]
lista_precisao = [2, 2, 3, 3]
gerenciar = lambda x,y: round(x, y)
numeros_redizidos = list(map(gerenciar, lista_numeros, lista_precisao))
print(numeros_redizidos)
'''

# somar toda a lista com programação funcional
from functools import reduce
numeros = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 , 10]
somador = lambda x, y: x + y
numeros_somados = reduce(somador, numeros)
print(f'Os numeros somados foram: {numeros_somados}')