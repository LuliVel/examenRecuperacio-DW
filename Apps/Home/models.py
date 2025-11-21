from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
	perfil = models.OneToOneField(User, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.perfil.username

@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
	if created:
		Cliente.objects.create(perfil=instance)

@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, **kwargs):
	if hasattr(instance, 'cliente'):
		instance.cliente.save()
