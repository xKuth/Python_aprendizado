from datetime import date
nascimento = int(input('Qual o ano do seu nascimento? '))
ano = date.today().year - nascimento
if ano <= 9:
    print('Sua categoria é: \033[1;32mMIRIM\033[m')
elif (ano <= 14) and (ano > 9):
    print('Sua categoria é: \033[1;32mINFANTIL\033[m')
elif ano <= 19:
    print('Sua categoria é: \033[1;32mJUNIOR\033[m')
elif ano <= 25:
    print('Sua categoria é: \033[1;32mSENIOR\033[m')
else:
    print('Sua categoria é: \033[1;32mMASTER\033[m')

