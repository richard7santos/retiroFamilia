# Generated by Django 5.0.1 on 2024-02-22 01:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0030_alter_inscricoes_total_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='comprovante_pagamento',
            field=models.FileField(upload_to='comprovantes/'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='data_pagamento',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
