from django.db import models

# Create your models here.
class GabrielNode(models.Model):
    sensor = models.BooleanField()
    botao = models.BooleanField()
    liga_robo = models.BooleanField()
    reset_contador = models.BooleanField()
    valor_contagem = models.IntegerField()