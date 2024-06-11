try:
    a = int(input('numerador: '))
    b = int(input('denominador '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado e {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado')
'''except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')'''