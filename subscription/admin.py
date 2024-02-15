from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Sum

from subscription.models import Inscricoes, Pagamento

# actions
@admin.action(description='Aprovar pagamentos selecionados')
def aprovar_pagamento(modeladmin, request, queryset):
   for obj in queryset:
      obj.status = 'Aprovado'
      obj.save()


@admin.action(description='Reprovar pagamentos selecionados')
def reprovar_pagamento(modeladmin, request, queryset):
   for obj in queryset:
      obj.status = 'Reprovado'
      obj.save()
 
# displays
class InscricoesAdmin(admin.ModelAdmin):
   list_display = ('nome_inscrito', 'valor_inscricao', 'total_pago') 

class PagamentoAdmin(admin.ModelAdmin):
   list_display = ('inscricao','data_pagamento', 'valor', 'comprovante_pagamento', 'status' )
   actions = [aprovar_pagamento, reprovar_pagamento ]
   

admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Inscricoes, InscricoesAdmin)

