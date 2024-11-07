from django.urls import path
from . import views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pedido'

urlpatterns = [
    path('', views.Pagar, name='pagar'),
    path('carrinho/', views.Carrinho, name='carrinho'),
    path('addcarrinho/<int:id>/', views.AddCarrinho, name='addcarrinho'),
    path('addcarrinhodig/', views.AddCarrinhoDig, name='AddCarrinhoDig'),
    path('removercarrinho/<int:id>/', views.RemoverCarrinho, name='removercarrinho'),
    path('removercarrinhodig/', views.RemoverCarrinhoDig, name='removercarrinhodig'),
    path('continuarcarrinho/<int:id>/', views.ContinuarCarrinho, name='continuarcarrinho'),
    path('continuarcarrinhodig/', views.ContinuarCarrinhoDig, name='continuarcarrinhodig'),
    path('resumo/', views.Resumo, name='resumo'),
    
    #path('fecharpedido/', views.FecharPagar, name='fecharpagar'),
]
