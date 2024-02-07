# Generated by Django 5.0.1 on 2024-02-02 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0005_alter_pagamento_comprovante_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='inscrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamentos', to='subscription.inscricoes'),
        ),
    ]