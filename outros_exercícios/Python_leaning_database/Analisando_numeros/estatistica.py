with open('numeros_sorteados.txt', 'r') as numeros:
    valores = numeros.read()
    r = valores.split()
    print(len(r))
    for i, elem in enumerate(r):
        print(elem)
