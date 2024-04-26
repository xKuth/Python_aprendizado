p = float(input('Qual o valor do produto? '))
des = p * 0.05
novovalor = p - des
# outro de jeito de fazer apenas com uma linha novo = (p * 5 / 100)
print('O produto custa {} e com desconto vai valer {:.2f}'.format(p,novovalor))