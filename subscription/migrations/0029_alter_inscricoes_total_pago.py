# Generated by Django 5.0.1 on 2024-02-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0028_pagamento_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricoes',
            name='total_pago',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]