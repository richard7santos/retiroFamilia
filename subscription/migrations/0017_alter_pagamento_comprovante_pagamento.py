# Generated by Django 5.0.1 on 2024-02-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0016_alter_pagamento_comprovante_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='comprovante_pagamento',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]