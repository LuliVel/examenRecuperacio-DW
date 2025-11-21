from django.urls import path
from . import views

app_name = 'Home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homeapp'),
    path('creditos/', views.CreditosView.as_view(), name='creditos'),
    path('usuarios/', views.UsuariosView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>/', views.VerUsuarioView.as_view(), name='ver_usuario'),
    path('usuarios/<int:pk>/eliminar/', views.EliminarUsuarioView.as_view(), name='eliminar_usuario'),
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('login/', views.LoginView.as_view(), name='login'),
    
]
