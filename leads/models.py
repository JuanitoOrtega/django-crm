from django.db import models
# from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Agent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')

  def __str__(self):
    return self.user.username

  class Meta:
    verbose_name = 'Agente'
    verbose_name_plural = 'Agentes'


class Lead(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Nombres')
    last_name = models.CharField(max_length=20, verbose_name='Apellidos')
    age = models.IntegerField(default=0, verbose_name='Edad')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Agente')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'