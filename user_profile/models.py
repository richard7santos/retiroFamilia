from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=16, null=True)
    foto = models.ImageField(null=True, blank=True, verbose_name='Imagem')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        if self.nome_completo:
            return self.nome_completo
        else:
            return self.usuario.username
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
    

