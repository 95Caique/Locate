# Generated by Django 5.0.1 on 2024-02-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_imovel_imovelimagens_registrarlocacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='tipo_item',
            field=models.CharField(choices=[('APARTAMENTO', 'Apartemento'), ('KITNET', 'Kitnet'), ('CASA', 'Casa')], max_length=100),
        ),
    ]
