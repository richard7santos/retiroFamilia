from django import forms

from subscription.models import Inscricoes, Pagamento

class InscricoesForm(forms.ModelForm):
    class Meta:
        model = Inscricoes
        fields = '__all__'
    
class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'