import requests
verificacao = 'https://www.uta-net.com/song/330976/'
try:
    if requests.get(verificacao).status_code == 200:
        print('o site esta funcionanado!')
except ConnectionError:
    print('O site está fora do ar')


# Solução do Gustavo guanabara
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não esta acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')'''

