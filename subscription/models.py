from django.db import models

class Pagamento(models.Model):
    data_pagamento= models.DateField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    comprovante_pagamento = models.FileField(upload_to ='uploads/')

    def __str__(self):
        return str(self.data_pagamento)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

class Inscricoes(models.Model):
    nome_inscrito = models.CharField(max_length=50)
    idade = models.IntegerField(default=0)
    dt_inscricao = models.DateField
    responsável = models.CharField(max_length=50)
    RESPONSAVEL_CHOICES = (
        ("Pai", "Pai"),
        ("Mãe", "Mãe"),
        ("Responsável legal", "Responsavel legal")
    )
    parentesco_responsável = models.CharField(max_length=50, choices = RESPONSAVEL_CHOICES, blank= True, null=True)

    ESTADO_CIVIL_CHOICES = (
        ("Casado", "Casado"),
        ("Solteiro", "Solteiro"),
        ("Namorando", "Namorando")
    )
    estado_civil = models.CharField(max_length=20, choices = ESTADO_CIVIL_CHOICES, default="Em avaliação", blank=True )
    valor_inscricao = models.DecimalField(max_digits=5, decimal_places=2)
    pagamento = models.ForeignKey(Pagamento, on_delete = models.CASCADE)

    STATUS_CHOICES = (
        ("Pago", "Pago"),
        ("Pagamento parcelado", "Pagamento parcelado"),
    )
    status = models.CharField(max_length=50, choices = STATUS_CHOICES, blank= True, null=True)

    def __str__(self):
        return self.nome_inscrito
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
