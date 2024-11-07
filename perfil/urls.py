from . import views
from django.urls import path
from . import views
from django.conf import settings


app_name = 'perfil'

urlpatterns = [
    path('criar/', views.criar_usuario_view, name='criar'),
]


