final = {'total': 0, 'maior': 0, 'menor': 0, 'média': 0}


def notas(*num, **situacao):
    """
    :parameter situacao: Para ver a situação do aluno, sit=true
    :param num: Todas media declaradas.
    :return: Retorna o 'final' com todas Notas , maior e menor e a média.
    """
    final['total'] = len(num)
    maior = menor = contador = 0
    for cont in range(0, len(num)):
        contador += num[cont]
        if cont == 0:
            maior = menor = num[cont]
        if num[cont] > maior:
            maior = num[cont]
        elif num[cont] < menor:
            menor = num[cont]
    media = contador / len(num)
    final['média'] = media
    final['menor'] = menor
    final['maior'] = maior
    if situacao:
        if media >= 6:
            final['Situação'] = 'Aprovado'
        elif 4 <= media <= 6:
            final['Situação'] = 'recuperação'
        else:
            final['Situação'] = 'Reprovado'
    return final


alunos = notas(4, 2, 5, sit=True)
print(alunos)
