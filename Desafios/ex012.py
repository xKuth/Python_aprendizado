p = float(input('Qual o valor do produto? '))
des = p * 0.05
novovalor = p - des
# outro de jeito de fazer apenas com uma linha novo = (p * 5 / 100)
print('O produto custa \033[1;31m{}\033[m e com desconto vai valer \033[1;31m{:.2f}\033[m'.format(p,novovalor))