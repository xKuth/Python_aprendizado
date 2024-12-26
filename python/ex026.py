frase = str(input('Qual frase deseja Verificar? ')).strip()
frasecon = frase.upper()
print('A letra "A" aparece \033[0;35m{}\033[m vezes'.format(frasecon.count('A')))
print('A primeira letra "A" aparece primeira vez na posição \033[0;35m{}\033[m'.format(frasecon.find('A')+1))
print('A posição do ultimo "A" é \033[0;35m{}\033[m'.format(frasecon.rfind('A')+1))

#Solução do Gustavo Guanabara

'''frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece \033[0;35m{}\033[m na frase'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição \033[0;35m{}\033[m'.format(frase.find('A')+1))
print('A ultima letra "A" apareceu na posição \033[0;35m{}\033[m'.format(frase.rfind('A')+1))'''
