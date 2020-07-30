from django.db import models

# Create your models here.


class ImpostoDeRenda(models.Model):
    rendimento_a = models.FloatField()
    rendimento_b = models.FloatField()
    isento = models.BooleanField()
    aliquota = models.FloatField()
    deducao = models.FloatField()
    ano_referencia = models.IntegerField()
