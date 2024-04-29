reta1 = float(input('Digite a primeira reta: '))
reta2 = float(input('Digite a segunda reta: '))
reta3 = float(input('Digite a terceira reta: '))
somatriangulos = reta1 + reta2
if somatriangulos > reta3:
    print('É possivel formar um \033[0;31mTriangulo\033[m')
else:
    print('Não é possivel formar um \033[0;31mTriangulo\033[m')

#Solução do Gustavo Guanabara
'''print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + 3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima Podem Formar \033[0;31mTriângulo\033[m!')
else:
    print('Os segmentos acima NÃo podem formar \033[0;31mTriângulo\033[m')'''