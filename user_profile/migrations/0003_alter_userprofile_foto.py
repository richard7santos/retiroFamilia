# Generated by Django 5.0.1 on 2024-02-22 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='user_photos/', verbose_name='Imagem'),
        ),
    ]
