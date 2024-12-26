lado1 = float(input('Qual a primeira medida? '))
lado2 = float(input('Qual a segunda medida? '))
lado3 = float(input('Qual a terceira medida? '))
triangulo = lado1 + lado2
triangulo2 = lado3 + lado2

if (lado1 == lado2 ) and (lado1 == lado3):
    print('Esse é um \033[0;33;40mTRIANGULO EQUILÁTERO\033[m ,todos lados iguais')
elif (triangulo >= lado3) and (triangulo2 > lado1) and (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print('Esse é um \033[0;33;40mTRIANGULO ISÓSCELES\033[m ,dois lados dele são iguais')
elif (triangulo >= lado3) and (triangulo2 >= lado1):
    print('Esse é um \033[0;33;40mTRIÂNGULO ESCALENO\033[m ,todos lados diferentes')
else:
    print('Não é possivel formar um \033[0;33;40mTRIÂNGULO\033[m com essas medidas')

#solução do Gustavo Guanabara
'''r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r3 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um Triângulo', end=' ')
    if r1 == r2 == r3:
      print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO')'''