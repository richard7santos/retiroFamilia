from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from core.forms import UserForm
from user_profile.models import UserProfile
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout

class UserCreate(CreateView):
    template_name = 'partials/forms.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        group = get_object_or_404(Group, name='inscritos')
        url = super().form_valid(form)
        self.object.groups.add(group)
        self.object.save()
        UserProfile.objects.create(usuario=self.object)
        
        return url
        
    def get_context_data(self, *args, **kwargs: Any):
        context = super().get_context_data( *args, **kwargs)

        context['title'] = "Registro de Usuário"
        context['button'] = "Cadastrar"

        return context

def home(request):
    return render(request, 'index.html')

def userLogout(request):
    logout(request)
    return render(request,'index.html')

class UserProfileUpdate(UpdateView):
    template_name = 'partials/forms.html'
    model = UserProfile
    fields = ['nome_completo', 'telefone', 'foto']
    success_url = reverse_lazy('home')

    def get_object(self, queryset= None):
        self.object = get_object_or_404(UserProfile, usuario = self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs: Any):
        context = super().get_context_data( *args, **kwargs)

        context['title'] = "Meus dados"
        context['button'] = "Atualizar"

        return context
        
