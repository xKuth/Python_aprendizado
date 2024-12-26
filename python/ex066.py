n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número inteiro (digite 999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos \033[1;33m{cont}\033[m números foi \033[1;33m{soma}\033[m')