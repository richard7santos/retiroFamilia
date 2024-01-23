from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=16, null=True)
    foto = models.ImageField(upload_to='fotos_usuarios', null=True, blank=True, verbose_name='Imagem')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
