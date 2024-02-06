from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Inscricoes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nome_inscrito = models.CharField(max_length=50, verbose_name= 'Nome completo')
    idade = models.IntegerField(default=0)
    dt_inscricao = models.DateTimeField(default=timezone.now)
    telefone_1 = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone 1')
    telefone_2 = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone 2')
    email = models.EmailField(null=True, blank=True, verbose_name='E-mail')
    responsavel = models.CharField(max_length=50, verbose_name= 'Responsável (Se menor de 18 anos)', blank=True, default="-")
    cep = models.CharField(max_length=11, null=True, blank=True)
    logradouro = models.CharField(max_length=200, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True, default=0)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    uf = models.CharField(max_length=100, null=True, blank=True)
    RESPONSAVEL_CHOICES = (
        ("Pai", "Pai"),
        ("Mãe", "Mãe"),
        ("Responsável legal", "Responsavel legal")
    )
    parentesco_responsável = models.CharField(max_length=50, choices = RESPONSAVEL_CHOICES, blank= True, null=True, verbose_name= 'Parentesco')

    ESTADO_CIVIL_CHOICES = (
        ("Casado", "Casado"),
        ("Solteiro", "Solteiro"),
        ("Namorando", "Namorando")
    )
    estado_civil = models.CharField(max_length=20, choices = ESTADO_CIVIL_CHOICES )
    valor_inscricao = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    STATUS_CHOICES = (
        ("Pago", "Pago"),
        ("Pagamento parcelado", "Pagamento parcelado"),
    )
    status = models.CharField(max_length=50, choices = STATUS_CHOICES,  default="Pagamento parcelado", blank= True)

    def formatted_date(self):
        self.dt_inscricao = self.dt_inscricao - timedelta(hours=3)
        return self.dt_inscricao.strftime("%d/%m/%y")

    def __str__(self):
        return self.nome_inscrito
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

class Pagamento(models.Model):
    inscricao = models.ForeignKey(Inscricoes, on_delete = models.CASCADE, related_name='pagamentos', blank=True)
    data_registro= models.DateTimeField(default=timezone.now, blank=True, null=True)
    data_pagamento = models.CharField(max_length=12)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    comprovante_pagamento = models.FileField(upload_to ='uploads/', blank=True, null=True)

    def formatted_date(self):
        self.data_registro = self.data_registro - timedelta(hours=3)
        return self.data_registro.strftime("%d/%m/%y %Hh%M")

    def __str__(self):
        return str(self.data_pagamento)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'