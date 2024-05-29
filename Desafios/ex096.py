def area():
    print(f'o total da área é de {lar}x{comp} é de {lar * comp:.2f}m²')


print('  CONTROLE DE TERRENOS  ')
print('------------------------')
lar = float(input('Qual a largura da área? '))
comp = float(input('qual o comprimento da área? '))
area()