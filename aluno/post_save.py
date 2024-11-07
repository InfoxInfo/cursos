from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Aluno
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_aluno_profile(sender, instance, created, **kwargs):
    if created:
        Aluno.objects.create(user=instance)