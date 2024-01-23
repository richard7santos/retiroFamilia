from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from core.forms import UserForm
from django.shortcuts import get_object_or_404

class UserCreate(CreateView):
    template_name = 'partials/forms.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        group = get_object_or_404(Group, name='inscritos')
        url = super().form_valid(form)
        self.object.groups.add(group)
        self.object.save()
        return url
        
    def get_context_data(self, *args, **kwargs: Any):
        context = super().get_context_data( *args, **kwargs)

        context['title'] = "Registro de Usuário"
        context['button'] = "Cadastrar"

        return context

def home(request):
    return render(request, 'index.html')
