from django.urls import path
from subscription.views import add_pagamento, delete_incricao, detalhe_incricao, edit_incricao, list_incricao, add_incricao

urlpatterns = [
    path('', add_incricao, name='inscrever'),
    path('edit/<int:id>', edit_incricao, name='atualizar'),
    path('list/', list_incricao, name='incricoes_list'),
    path('delete/<int:id>', delete_incricao, name='incricoes_delete'),
    path('pagar/<int:id>', add_pagamento, name='incricoes_pagar'),
    path('datalhe/<int:id>', detalhe_incricao, name='incricoes_detalhe'),
]
