from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import (
    Aluno,
    Inscricao,
    Licao,
    Curso,
    Digitacao,
    InscricaoDigitacao,
    DigitacaoDetalhes,
    ItemQuestao,
    Questao,
)

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        # Especifique os campos que deseja incluir no formulário
        fields = ['nome_completo','genero', 'endereco', 'numero','complemento','bairro','cep','cidade','estado', 'telefone', 'email', 'data_nascimento', 'cpf', 'foto']

        widgets = {
            'imagem': forms.FileInput(),
        }

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

        widgets = {
            'imagem': forms.FileInput(),
        }
        
class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['aluno', 'curso', 'categoria_licao']

    def __init__(self, *args, **kwargs):
        super(InscricaoForm, self).__init__(*args, **kwargs)
        # Personalize o queryset para o campo "aluno" para ordená-lo por ordem alfabética
        self.fields['aluno'].queryset = User.objects.order_by('username')


class LicaoForm(ModelForm):
    class Meta:
        model = Licao
        fields = '__all__'


class DigitacaoForm(ModelForm):
    class Meta:
        model = Digitacao
        fields = '__all__'

class DigitacaoDetalhesForm(ModelForm):
    class Meta:
        model = DigitacaoDetalhes
        fields = '__all__'

class InscricaoDigitacaoForm(ModelForm):
    class Meta:
        model = InscricaoDigitacao
        fields = '__all__'


class ItemQuestaoForm(ModelForm):
    class Meta:
        model = ItemQuestao
        fields = '__all__'


class QuestaoForm(ModelForm):
    class Meta:
        model = Questao
        fields = '__all__'
