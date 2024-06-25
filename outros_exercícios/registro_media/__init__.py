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


