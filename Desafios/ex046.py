from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    print('Os fogos vão estourar em \033[1;33m{}s\033[m'.format(c))
print('-='*10)
print('Boooommmmm♦♦♦♦')