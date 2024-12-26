metr = float(input('Qual o valor em metros? '))
km = metr / 1000
hm = metr / 100
dam = metr / 10
dm = metr * 10
cent = metr * 100
milim = metr * 1000
print('A medida de {0}m corresponde a'.format(metr))
cores = {'magenta': '\033[4;35m', 'limpa': '\033[m'}
print('{6}{0}{7}km \n{6}{1}{7}hm \n{6}{2}{7}dam \n{6}{3}{7}dm \n{6}{4}{7}cm \n{6}{5}{7}mm'.format(km,hm,dam,dm,cent,milim, cores['magenta'], cores['limpa'] ))