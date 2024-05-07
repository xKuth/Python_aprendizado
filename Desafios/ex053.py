frase = str(input('Digite uma frase: ')).strip()
frase_inteira = frase.split()
frase_completa = ''.join(frase_inteira).upper()
nova_frase = frase_completa[::-1]

if nova_frase == frase_completa:
    print('Essa frase é políndroma')
else:
    print('Essa frase não é polindroma')

'''#Solução do Gustavo Guanabara
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#Ou você pode usar estrutura de repitação com fatiamento com abaixo:
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo!')
else:
    print('A frase digitada não é um palíndromo')'''