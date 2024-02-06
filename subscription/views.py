from django.db.models.base import Model as Model
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse
from subscription.forms import InscricoesForm, PagamentoForm
from subscription.models import Inscricoes, Pagamento
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def list_incricao(request):
    inscricoes = Inscricoes.objects.filter(user=request.user)
    return render(request, 'inscricoes_list.html', {'inscricoes': inscricoes })

@login_required()
def add_incricao(request):
     
    form = InscricoesForm()
    context = {
            'title': "Formulário de Inscrição",
            'button': "Inscrever-se",
            'subtitle': "Registro de Pagamentos",
            'form': form,
    }
        
    if request.method == "POST":

        form = InscricoesForm(data=request.POST)

        if form.is_valid():

            insc = form.save(commit=False)
            insc.user = request.user
            estadocivil = insc.estado_civil
            responsavel = insc.responsavel
            if estadocivil == 'Casado':
                insc.valor_inscricao = 1300.00
            else:
                insc.valor_inscricao = 500.00

            if(responsavel == "-"):
               insc.responsavel = insc.nome_inscrito

            insc.save()
            messages.success(request, "SUCESSO: Inscrição realizada com sucesso.")
            return redirect('incricoes_list')
        else:
            messages.error(request, "ERRO: Ocorreu um erro ao realizar inscrição")
            
    return render(request, "inscricoes_form.html", context)

@login_required()
def edit_incricao(request, id):

    inscricao = get_object_or_404(Inscricoes, pk=id, user=request.user)
    form = InscricoesForm(request.POST or None, request.FILES or None, instance=inscricao)

    context = {
        'title': "Atualizar Inscrição",
        'button': "Atualizar",
        'form': form
    }
    if request.method == "POST":
        form = InscricoesForm(request.POST or None, request.FILES or None, instance=inscricao)

        if form.is_valid():
            insc = form.save(commit=False)
            insc.user = request.user
            estadocivil = insc.estado_civil
            if estadocivil == 'Casado':
                insc.valor_inscricao = 1300.00
            else:
                insc.valor_inscricao = 500.00

            insc.save()
            messages.success(request, "SUCESSO: Inscrição Atualizada com sucesso.")
            return redirect('incricoes_list')
        else:
            messages.error(request, "ERRO: Ocorreu um erro ao Atualizar inscrição")
    
    return render(request, 'inscricoes_form.html', context )

@login_required()
def delete_incricao(request, id):

    inscricao = get_object_or_404(Inscricoes, pk=id, user=request.user)

    if request.method == "POST":
        inscricao.delete()
        messages.success(request, "SUCESSO: Inscrição deletada com sucesso.")
        return redirect('incricoes_list')
        
    return render(request, 'confirmation_delete_inscricao.html', {'inscricao': inscricao} )

@login_required()
def detalhe_incricao(request, id):
    inscricao = get_object_or_404(Inscricoes, pk=id, user=request.user)   
    return render(request, 'inscricoes_details.html', {'inscricao': inscricao} )

# # Pagamentos

def add_pagamento(request, id):
    form = PagamentoForm()
    inscricao = get_object_or_404(Inscricoes, pk=id)
    context = {
        'title': "Registrar um pagamento",
        'button': "Registrar",
        'form': form
    }
    if request.method == "POST":
        form = PagamentoForm(data=request.POST)
        if form.is_valid():
            pgto = form.save(commit=False) 
            pgto.inscricao = inscricao
            pgto.save()
            messages.success(request, "SUCESSO: Pagamento registrado com sucesso.")
            return redirect('incricoes_list')
        else:
            messages.error(request, "ERRO: Ocorreu um erro ao realizar inscrição")
    return render(request, 'partials/forms.html', context )

def list_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'inscricoes_details.html', {'pagamentos': pagamentos })