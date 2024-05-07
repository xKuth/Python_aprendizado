idade_maior = 0
mulher_menor = 0
soma = 0
mulher_menor = 0
for c in range(0 ,4):
    n1 = str(input('Qual é sue nome: '))
    idade = int(input('Qual sua idade: '))
    s = int(input('Qual é seu seu sexo: \n[1]-homem:\n[2]-mulher:'))
    soma = idade + soma
    if (idade > idade_maior) and (s == 1):
         idade_maior = idade
         nome_mais = n1
    if (s == 2) and (idade <= 20):
        mulher_menor = mulher_menor + 1
m = soma / 4
print('A média de idade dos grupo é {}'.format(m))
print('Qual é o nome do homem mais velho {}'.format(nome_mais))
print('Tem {}  mulheres com menos de 20 anos.'.format(mulher_menor))





