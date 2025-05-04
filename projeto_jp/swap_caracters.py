import re
lista_jp = []


with open('Vocalu.txt', 'r') as arq:
    japonese_pattern = re.compile('[\u3040-\u30FF\u4E00-\u9FFF]')
    text = arq.readline()
    japonese_pattern = japonese_pattern.findall(text)
    japonese_pattern.findall(text)
    japonese_text = find_text
    print(text)

