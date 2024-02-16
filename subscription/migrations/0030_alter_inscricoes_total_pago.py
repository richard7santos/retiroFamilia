# Generated by Django 5.0.1 on 2024-02-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0029_alter_inscricoes_total_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricoes',
            name='total_pago',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6),
        ),
    ]