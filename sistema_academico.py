def calcular_media(notas):
    """
    Calcula a média das notas de um estudante.

    Args:
        notas (list): Lista contendo as notas do estudante.

    Returns:
        float: Média calculada das notas.
    """

    soma_notas = sum(notas)
    quantidade_notas = len(notas)
    media = soma_notas / quantidade_notas

    return media


def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica se o estudante foi aprovado ou reprovado.

    Args:
        media (float): Média final do estudante.
        media_minima (float): Média mínima necessária para aprovação.

    Returns:
        str: Retorna 'Aprovado' ou 'Reprovado'.
    """

    if media >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"