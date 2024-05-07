peso = float(input('Qual é seu peso ?'))
altura = float(input('Qual é sua altura ?'))
imc = peso / (altura**2)
if imc < 18.5:
    print('Você esta \033[1;35mabaixo do peso ideal\033[m')
elif (imc >= 18.5) and (imc < 25):
    print('Você esta no \033[1;34mpeso ideal\033[m')
elif (imc >= 25) and (imc < 30):
    print('Você esta com \033[1;37mSobrepeso\033[m')
elif (imc >=30) and (imc < 40):
    print('Você esta na \033[1;31mObesidade\033[m')
else:
    print('você esta com \033[1;31mObesidade mórbida\033[m')