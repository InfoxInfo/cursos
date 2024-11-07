from django.conf import settings
from aluno.models import Aluno


def aluno(request):
    if request.user.is_authenticated:
        try:
            aluno = Aluno.objects.get(user=request.user)
        except Aluno.DoesNotExist:
            aluno = None
    else:
        aluno = None
    return {'aluno': aluno}