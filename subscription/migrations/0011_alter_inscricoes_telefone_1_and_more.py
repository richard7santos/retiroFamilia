# Generated by Django 5.0.1 on 2024-02-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0010_alter_inscricoes_bairro_alter_inscricoes_cep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricoes',
            name='telefone_1',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone 1'),
        ),
        migrations.AlterField(
            model_name='inscricoes',
            name='telefone_2',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone 2'),
        ),
    ]