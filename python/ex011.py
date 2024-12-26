lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
t = lar * alt
tinta = t / 2
print('Você vai precisar de \033[1;31m{0}\033[m litros de tinta'.format(tinta))