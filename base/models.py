from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return "{} - {}".format(self.nome, self.email)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-id']

class TipoImovel(models.TextChoices):
    APARTEMENTO = 'APARTAMENTO, APARTAMENTO'
    KITNET = 'KITNET, KITNET'
    CASA = 'CASA, CASA'

class Codigo(models.Model):
    codigo = models.CharField(max_length=100)
    tipo_item = models.CharField(max_length=100, choices=Type)
