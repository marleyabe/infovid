from django.db import models

# Create your models here.

class Dados(models.Model):
    estado = models.CharField('Estado', max_length=200)
    casos = models.CharField('Estado', max_length=200)
    mortes = models.CharField('Estado', max_length=200)
    novos_casos = models.CharField('Estado', max_length=200)