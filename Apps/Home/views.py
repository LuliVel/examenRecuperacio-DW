from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CreditosView(TemplateView):
    template_name = 'creditos.html'

class HomeView(TemplateView):
    template_name = 'index.html'

from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from .models import Cliente

class UsuariosView(ListView):
    model = Cliente
    template_name = 'usuarios.html'
    context_object_name = 'clientes'

class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'registro.html'
    success_url = reverse_lazy('Home:login')

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('Home:homeapp')