from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import (
    InfoxModel,
    CursoSuperior,
    CursoS,
    CursoSuper,
    CursoTecnico,
    PosGraduacao,
    MBA,
    LogoEmpresas,
    CursoProf,
    LogoEmpresasProf,
    Curso,
    Pacote,
    Turma,
    Equipefoto,
    ContactMe,
)

class InfoxForm(ModelForm):
    class Meta:
        model = InfoxModel
        fields = '__all__'
        
        widgets = {
            'imagem': forms.FileInput(),
            'equipeImagem': forms.FileInput(),
        }

class CursoSuperiorForm(ModelForm):
    class Meta:
        model = CursoSuperior
        fields = '__all__'

        widgets = {
            'logo': forms.FileInput(),
            'imagemCapa': forms.FileInput(),
            'imagemTutora': forms.FileInput(),
            'logo_empresa': forms.FileInput(),
        }

class CursoSForm(ModelForm):
    class Meta:
        model = CursoS
        fields = '__all__'
        
        widgets = {

        }

class CursoSuperForm(ModelForm):
    class Meta:
        model = CursoSuper
        fields = ['curso', 'descricao']


class CursoTecnicoForm(ModelForm):
    class Meta:
        model = CursoTecnico
        fields = '__all__'
        
        widgets = {

        }
    
class PosGraduacaoForm(ModelForm):
    class Meta:
        model = PosGraduacao
        fields = '__all__'
        
        widgets = {

        }
    
class MBAForm(ModelForm):
    class Meta:
        model = MBA
        fields = '__all__'
        
        widgets = {

        }

class LogoEmpresasForm(ModelForm):
    class Meta:
        model = LogoEmpresas
        fields = '__all__'
        
        widgets = {
            'logo_empresa': forms.FileInput(),
        }

class CursoProfForm(ModelForm):
    class Meta:
        model = CursoProf
        fields = '__all__'
        
        widgets = {
            'imagem_logo': forms.FileInput(),
            'imagem_capa': forms.FileInput(),
        }

class LogoEmpresasProfForm(ModelForm):
    class Meta:
        model = LogoEmpresasProf
        fields = '__all__'
        
        widgets = {
            'logo_empresa_prof': forms.FileInput(),
        }

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class PacoteForm(ModelForm):
    class Meta:
        model = Pacote
        fields = '__all__'

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'

class EquipefotoForm(ModelForm):
    class Meta:
        model = Equipefoto
        fields = '__all__'

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ['name', 'email', 'subject', 'message']  # Corrigi o nome do campo 'messege' para 'message'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'