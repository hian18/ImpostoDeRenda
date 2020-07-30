from . import models


def find_imposto_de_renda_by_rendimento(rendimento):
    result = models.ImpostoDeRenda.objects.filter(
        rendimento_a__lte=rendimento).order()
    return result
