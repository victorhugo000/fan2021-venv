# Generated by Django 3.1.7 on 2021-04-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoconstrucao', '0009_remove_venda_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='eletricos',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='venda',
            name='nome',
            field=models.CharField(max_length=255, null=True, verbose_name='Nome do produto'),
        ),
    ]
