from django.db import models
from django.contrib.auth.models import User
from aluno.models import Curso as Curso

class Carrinho(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso, through='ItemCarrinho')

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)