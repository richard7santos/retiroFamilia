from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save, post_delete
from django.db.models.aggregates import  Sum


class Inscricoes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nome_inscrito = models.CharField(max_length=50, verbose_name= 'Nome completo')
    conjuge = models.CharField(max_length=50, verbose_name= 'Nome do cônjuge', null=True, blank=True)
    idade = models.IntegerField(default=0)
    idade_conjuge = models.IntegerField(default=0, verbose_name= 'Idade do cônjuge', null=True, blank=True)
    dt_inscricao = models.DateTimeField(default=timezone.now, verbose_name= 'Data de inscrição', blank=True)
    telefone_1 = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone 1')
    telefone_2 = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone 2')
    email = models.EmailField(null=True, blank=True, verbose_name='E-mail')
    responsavel = models.CharField(max_length=50, verbose_name= 'Responsável', blank=True, null=True)
    cep = models.CharField(max_length=11, null=True, blank=True)
    logradouro = models.CharField(max_length=200, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True, default=0)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    uf = models.CharField(max_length=100, null=True, blank=True)
    total_pago = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0.0 )
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
    inscricao = models.ForeignKey(Inscricoes, on_delete = models.CASCADE, blank=True, null=True)
    data_registro= models.DateTimeField(default=timezone.now, blank=True, null=True)
    data_pagamento = models.DateTimeField(default=timezone.now, blank=True, null=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    comprovante_pagamento = models.FileField(upload_to ='comprovantes/')
    STATUS_CHOICES = (
        ("Aprovado", "Aprovado"),
        ("Pendente de conferência", "Pendente de conferência"),
        ("Reprovado", "Reprovado"),
    )
    status = models.CharField(max_length=50, choices = STATUS_CHOICES,  default="Pendente de conferência", blank= True)
    def formatted_date(self):
        self.data_registro = self.data_registro - timedelta(hours=3)
        return self.data_registro.strftime("%d/%m/%y %Hh%M")

    def __str__(self):
        return str(self.valor)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

def atualiza_total_pago(sender, instance, created, **kwargs):
    pagamentos = Pagamento.objects.filter(inscricao=instance.inscricao)
    qtd_pgtos = len(pagamentos)

    if (qtd_pgtos != 0):
        total_pago = Pagamento.objects.filter(inscricao=instance.inscricao, status='Aprovado').aggregate(total=Sum('valor'))
        total_pago = total_pago['total']
        if total_pago:
            instance.inscricao.total_pago =float(total_pago)
            print('Passei no if e atualizei o valor')
        else:
            instance.inscricao.total_pago = 0.0
            print('Passei no else e zerei')
        instance.inscricao.save()
        

post_save.connect(atualiza_total_pago, sender=Pagamento)
