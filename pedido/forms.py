from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from aluno.models import Aluno



class PerfilForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        exclude = ('user',)

class UserForm(ModelForm):
    class Meta:
        model = User
        fiels = ('first_name', 'last_name', 'username', 'password', 'email')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data