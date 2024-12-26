vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80) * 7
    print('Você vai pagar R$\033[4;31;40m{}\033[m de multa'.format(multa))
else:
    print('Você esta dentro da velocidade PARABENS!')

#Solução do Gustavo Guanabara
'''velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Você execeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R$\033[4;31;40m{:.2f}\033[m'.format(multa))
print('Tenha um bom dia! Dirija com segurança')'''
