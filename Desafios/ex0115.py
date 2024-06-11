from ex115.dados import fmenu, pessoascadastros, novaspessoas
listapessoas = []
pessoas = []
fselecao = 0
while True:
    if fselecao == 3:
        break
    fselecao = fmenu()
    if fselecao == 1:
        pessoascadastros()
    if fselecao == 2:
        fselecao = novaspessoas()
    if fselecao == 3:
        print('-'*30)
        print(f'{"":>2}Saindo do sistema até logo!')
        print('-'*30)
        break
print()
