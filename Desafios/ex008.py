metr = float(input('Qual o valor em metros? '))
km = metr / 1000
hm = metr / 100
dam = metr / 10
dm = metr * 10
cent = metr * 100
milim = metr * 1000
print('A medida de {0}m corresponde a'.format(metr))
print('{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(km,hm,dam,dm,cent,milim))