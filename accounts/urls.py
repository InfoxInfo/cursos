from django.urls import path, include
from . import views

urlpatterns = [
        path('register', views.SingUp.as_view(), name="signup"),
        path('', include('django.contrib.auth.urls')),
]
