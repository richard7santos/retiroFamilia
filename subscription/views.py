from django.db.models.base import Model as Model
from django.shortcuts import redirect, render
from subscription.forms import InscricoesForm, PagamentoForm
from subscription.models import Inscricoes, Pagamento
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Avg, Sum, Count


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
    pagamentos = Pagamento.objects.filter(inscricao=inscricao)
    qtd_pgtos = len(pagamentos)

    if (qtd_pgtos != 0):
        total_pago = Pagamento.objects.filter(inscricao=inscricao).aggregate(total=Sum('valor'))
        total_pago = float(total_pago['total'])
    else:
        total_pago = 0.0

    context = {
        'inscricao': inscricao,
        'pagamentos': pagamentos,
        'total_pago': total_pago,  
    }
    return render(request, 'inscricoes_details.html', context )

# # Pagamentos

def add_pagamento(request, id):
    form = PagamentoForm()
    context = {
        'title': "Registrar um pagamento",
        'button': "Registrar",
        'button2': "Cancelar",
        'form': form
    }
    if request.method == "POST":
        form = PagamentoForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            inscricao_pgto = get_object_or_404(Inscricoes, pk=id)
            pgto = form.save(commit=False) 
            pgto.inscricao = inscricao_pgto
            pgto.save()
            messages.success(request, "SUCESSO: Pagamento registrado com sucesso.")
            return redirect('incricoes_list')
        else:
            messages.error(request, "ERRO: Ocorreu um erro ao registrar pagamento")
    return render(request, 'forms_pgto.html', context )

def pagamento_edit(request, id):
    pass

def pagamento_delete(request, id):
    pagamento = get_object_or_404(Pagamento, pk=id)

    if request.method == "POST":
        pagamento.delete()
        messages.success(request, "SUCESSO: Pagamento deletado com sucesso.")
        return redirect('incricoes_list')
        
    return render(request, 'confirmation_delete_pgto.html', {'pagamento': pagamento} )


