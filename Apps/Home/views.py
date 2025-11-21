from django.views.generic import DetailView, DeleteView
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.urls import reverse_lazy
from .models import Cliente
from django.contrib.auth.views import LoginView as DjangoLoginView

# Create your views here.
class CreditosView(LoginRequiredMixin, TemplateView):
    template_name = 'creditos.html'
    login_url = 'Home:login'

class HomeView(TemplateView):
    template_name = 'home.html'


class UsuariosView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'usuarios.html'
    context_object_name = 'clientes'
    login_url = 'Home:login'

class RegistroForm(UserCreationForm):
    telefono = forms.CharField(max_length=20, required=False, label='Teléfono')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('telefono',)

    def save(self, commit=True):
        user = super().save(commit)
        telefono = self.cleaned_data.get('telefono', '')
        if commit:
            Cliente.objects.filter(perfil=user).update(telefono=telefono)
        return user

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'registro.html'
    success_url = reverse_lazy('Home:login')



class LoginView(DjangoLoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('Home:usuarios')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, error_message="Usuario o contraseña incorrectos."))
class VerUsuarioView(DetailView):
    model = Cliente
    template_name = 'ver_usuario.html'
    context_object_name = 'cliente'

class EliminarUsuarioView(DeleteView):
    model = Cliente
    template_name = 'eliminar_usuario.html'
    success_url = reverse_lazy('Home:usuarios')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Usuario eliminado correctamente.")
        return super().delete(request, *args, **kwargs)