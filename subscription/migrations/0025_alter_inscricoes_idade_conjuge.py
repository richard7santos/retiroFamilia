# Generated by Django 5.0.1 on 2024-02-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0024_inscricoes_idade_conjuge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricoes',
            name='idade_conjuge',
            field=models.IntegerField(default=0, verbose_name='Idade do Cônjuge'),
        ),
    ]
