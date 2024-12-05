def medias(num):
    try:
        with open('media.txt', 'a') as totmedias:
            totmedias.write(f'\n{num}')
            totmedias.close()
    except KeyboardInterrupt:
        return 0
    except (ValueError, TypeError):
        print('Ocorreu um erro inesperado, tente novamente')
        return 0


def monstarmedias():
    with open('media.txt', 'r') as totmedias:
        todasM = totmedias.read().strip().split()
        for i in range(0, len(todasM)):
            print([i], 'º', todasM[i])


def mediaexistente(media_existente):
    with open('media.txt', 'r') as totmedias:
        for i in range(0, media_existente):
            if i == media_existente:
                pegarmedia = totmedias.readline()
        totmedias.close()
    return pegarmedia



