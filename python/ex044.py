produto = float(input('Qual o valor do produto? '))
print('[1]-Á vista dinheiro/cheque: 10% de desconto\n[2]-À vista no cartão: 5% de desconto')
print('[3]-Em até 2x no cartão: preço normal\n[4]-3x ou mais no cartão: 20% de juros')
escolha = int(input(''))
if escolha == 1:
    novo_produto = produto - (produto * 0.10)
    print('O produto com desconto de 10% passa a ser R$\033[0;32m{}\033[m'.format(novo_produto))
elif escolha == 2:
    novo_produto = produto - (produto * 0.05)
    print('O produto com deconto de 5% passa a ser R$\033[0;32m{}\033[m'.format(novo_produto))
elif escolha == 3:
    print('O produto esta no preço normal de R$\033[0;32m{}\033[m'.format(produto))
elif escolha == 4:
    divisao = int(input('De quantas vezes quer dividir? '))
    novo_produto = produto + (produto * 0.20)
    novo_produtodiv = novo_produto / divisao
    print('A partir de 3x aumenta 20% de juros')
    print('O produto no cartão de {}x aumenta e passa a valer R$\033[0;32m{}\033[m'.format(divisao, novo_produto))
    print('E você ira pagar {:.2f} por mes'.format(novo_produtodiv))
else:
    print('Você digitou uma opção incompativel')
