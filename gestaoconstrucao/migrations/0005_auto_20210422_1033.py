# Generated by Django 3.1.7 on 2021-04-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoconstrucao', '0004_auto_20210422_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(to='gestaoconstrucao.Hidraulico'),
        ),
    ]
