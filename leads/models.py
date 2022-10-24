from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


class Agent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
  organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Organización')

  def __str__(self):
    return self.user.email

  class Meta:
    verbose_name = 'Agente'
    verbose_name_plural = 'Agentes'


class Lead(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Nombres')
    last_name = models.CharField(max_length=20, verbose_name='Apellidos')
    age = models.IntegerField(default=0, verbose_name='Edad')
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Organización')
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Agente')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)