from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from subscription.forms import InscricoesForm
from subscription.models import Inscricoes
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
        'info': "É necessário estar logado para realizar uma inscrição",
        'form': form
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
    
    return render(request, 'inscricoes_form.html', context )

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