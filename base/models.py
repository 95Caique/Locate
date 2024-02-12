from django.db import models
from datetime import datetime

# Responsável por cadastrar clientes

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
    APARTEMENTO = 'APARTAMENTO'
    KITNET = 'KITNET'
    CASA = 'CASA'



class Imovel(models.Model):
    codigo = models.CharField(max_length=100, verbose_name='Código')
    tipo_item = models.CharField(max_length=100, choices=TipoImovel.choices)
    endereco = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    esta_locado = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.codigo, self.tipo_item)

    class Meta:
        verbose_name = 'Imovel'
        verbose_name_plural = 'Imoveis'
        ordering = ['-id']


class ImovelImagens(models.Model):
    imagem = models.ImageField('imagens', upload_to='images')
    imovel = models.ForeignKey(Imovel, related_name='imagem_imovel', on_delete=models.CASCADE)

    def __str__(self):
        return self.imovel.codigo

# Responsável por registrar a locação

class RegistrarLocacao(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='reg_locacao')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dt_start = models.DateTimeField('Inicio')
    dt_end = models.DateTimeField('Final')
    criado_em = models.DateTimeField(default=datetime.now, blank=True)

    def __srt__(self):
        return "{] - {}".format(self.cliente, self.imovel)

    class Meta:
        verbose_name = 'Registrar Locação'
        verbose_name_plural = 'Registrar Locação'
        ordering = ['-id']
