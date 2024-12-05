from time import sleep
from threading import Thread


# Entendendo como uma thread funciona
'''
def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando a taref{mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {mensagem}')


thread = Thread(target=tarefa, args=(2, 'thread em execução'))
thread.start()
print('\nAguardando pela execução da thread...')
thread.join()
print('A execução foi concluida!')
'''


# Entendendo a autenancia das threads
'''
def função_thread1(tempo_3, mensagem):
    print(f'Iniciando a thread, {mensagem}')
    sleep(tempo_3)
    print(f'\n\conclusão da: {mensagem} ')


thread1 = Thread(target=função_thread1, args=(3, 'A!'))
thread2 = Thread(target=função_thread1, args=(2, 'B'))
thread1.start()
thread2.start()
thread1.join()# Esperar ate completar a execução da thread 1
thread2.join()# Esperar ate completar a execução da thread 2
print('Execução finalizada')
'''

# fazendo calculo com duas Threads

'''def calcular_thread(tempo_espera, valor, mensagem):
    print(f'Iniciando a Thread! {mensagem}')
    sleep(tempo_espera)
    if mensagem == 'C':
        cal = valor ** 3
        print(f'O valor do {mensagem} foi {cal}')
    else:
        cal = valor ** 2
        print(f'O valor do {mensagem} foi {cal}')


cubo = Thread(target=calcular_thread, args=(3, 3, 'C'))
quadrado = Thread(target=calcular_thread, args=(2, 5, 'Q'))
cubo.start()
quadrado.start()
cubo.join()
quadrado.join()
print('Execução finalizada')'''

# Ou de outra forma

def calcular_cubo(tempo_espera, valor):
    print(f'Cubo: {valor ** 3}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_Cubo')

def calcular_quadrado(tempo_espera, valor):
    print(f'Quadradado: {valor ** 2}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_quadrado')
        

cubo = Thread(target=calcular_quadrado, args=(3, 5))
quadrado = Thread(target=calcular_cubo, args=(2, 5))
cubo.start()
quadrado.start()
cubo.join()# Esperar ate completar a execução da thread 1
quadrado.join()# Esperar ate completar a execução da thread 2
print('Execução foi concluida!')
