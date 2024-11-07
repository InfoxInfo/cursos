from django.shortcuts import get_object_or_404, render, redirect, render, redirect, reverse
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
from itertools import groupby
from aluno.models import Curso as CursoAluno, Inscricao, Licao, DigitacaoDetalhes

from infox.models import(
    InfoxModel,
    CursoSuperior,
    LogoEmpresas,
    CursoSuper,
    CursoTecnico,
    PosGraduacao,
    MBA,
    CursoProf,
    LogoEmpresasProf,
    Curso,
    Pacote,
    Turma,
    Equipefoto,
    ContactMe,
    )
from infox.forms import (
    InfoxForm,
    CursoSuperiorForm,
    CursoSForm,
    CursoSuperForm,
    CursoTecnicoForm,
    PosGraduacaoForm,
    MBAForm,
    LogoEmpresasForm,
    CursoProfForm,
    LogoEmpresasProfForm,
    CursoForm,
    PacoteForm,
    TurmaForm,
    EquipefotoForm,
    ContactMeForm,
)

@login_required
def site_detalhes(request):
    infox_lista = InfoxModel.objects.all()
    form = InfoxForm()
    data = {
        'infox_lista': infox_lista,
        'form': form,
    }
    return render(request, 'site_detalhes.html', data)


def infox_detalhes(request, id):
    infox = get_object_or_404(InfoxModel, id=id)
    fotoequipe = Equipefoto.objects.all()
    data = {
        'infox': infox,
        'fotoequipes': fotoequipe,
    }
    return render(request, 'infox_detalhes.html', data)



@login_required
def infox_lista(request, id):
    inscricao = get_object_or_404(InfoxModel, id=id)
    return render(request, 'infox_lista.html', {'inscricao': inscricao})


@login_required
def infox_novo(request):
    form = InfoxForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect('infox_detalhes')
    else:
        return render(request, 'infox_novo.html', {'form': form})  


@login_required
def infox_update(request, id):
    inscricao = get_object_or_404(InfoxModel, id=id)
    if request.method == 'POST':
        form = InfoxForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('infox_lista', id=inscricao.id)
    else:
        form = InfoxForm(instance=inscricao)
    
    return render(request, 'infox_update.html', {'inscricao': inscricao, 'form': form})

def sendmail_contact(data):
    messege_body = get_template('send.html').render(data)
    email = EmailMessage('Contato pelo Site',
                             messege_body, settings.DEFAULT_FROM_EMAIL,
                             to=['atendimento@cursosinfox.com.br'])
    email.content_subtype = "html"
    return email.send()

def contato_detalhes(request):
    email = ContactMe.objects.all()
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            form.save()
            # data, puxo as informações dos campos name, email, subject e message.
            data = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'subject': request.POST.get('subject'),
                'message': request.POST.get('message'),
            }
            sendmail_contact(data) # Cria função para envio
            
            return redirect('contato_enviado')
    else:
        form = ContactMeForm()
    
    return render(request, 'contato_detalhes.html', {'form': form, 'email': email})


def contato_enviado(request):
    return render(request, 'contato_enviado.html')


@login_required
def infox_equi_novo(request):
    if request.method == 'POST':
        form = EquipefotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('infox_equi_novo')
    else:
        form = EquipefotoForm()
    
    return render(request, 'infox_equi_novo.html', {'form': form})

@login_required
def infox_equi_lista(request):
    inscricoes = Equipefoto.objects.all()
    return render(request, 'infox_equi_lista.html', {'inscricoes': inscricoes})

@login_required
def infox_equi_update(request, id):
    inscricao = get_object_or_404(Equipefoto, id=id)
    if request.method == 'POST':
        form = EquipefotoForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('infox_equi_lista')
    else:
        form = EquipefotoForm(instance=inscricao)
    
    return render(request, 'infox_equi_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def infox_equi_delete(request, id):
    inscricao = get_object_or_404(Equipefoto, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('infox_equi_lista')
    return render(request, 'infox_equi_confirm_delete.html', {'inscricao': inscricao})


###### Categoria Superiores #######

def superior_detalhes(request):
    superior = CursoSuperior.objects.all()
    inscricoes = LogoEmpresas.objects.all()
    cursosuperior = CursoSuper.objects.all()
    cursotec = CursoTecnico.objects.all()
    pos = PosGraduacao.objects.all()
    mba = MBA.objects.all()
    form = CursoSuperForm()
    data = {
        'superior': superior,
        'form': form,
        'inscricoes': inscricoes,
        'cursosuperior': cursosuperior,
        'cursotec': cursotec,
        'pos': pos,
        'mba': mba,
    }
    return render(request, 'superior_detalhes.html', data)

def superior_novo(request):
    form = CursoSuperiorForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect('superior_detalhes')
    else:
        return render(request, 'superior_novo.html', {'form': form})

def superior_logo_novo(request):
    if request.method == 'POST':
        form = LogoEmpresasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('superior_logo_novo')
    else:
        form = LogoEmpresasForm()
    
    return render(request, 'superior_logo_novo.html', {'form': form})

@login_required
def superior_update(request, id):
    inscricao = get_object_or_404(CursoSuperior, id=id)
    if request.method == 'POST':
        form = CursoSuperiorForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('superior_lista', id=inscricao.id)
    else:
        form = CursoSuperiorForm(instance=inscricao)
    
    return render(request, 'superior_update.html', {'inscricao': inscricao, 'form': form})


@login_required
def superior_logo_update(request, id):
    inscricao = get_object_or_404(LogoEmpresas, id=id)
    if request.method == 'POST':
        form = LogoEmpresasForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('superior_logo_lista')
    else:
        form = LogoEmpresasForm(instance=inscricao)
    
    return render(request, 'superior_logo_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def superior_logo_delete(request, id):
    inscricao = get_object_or_404(LogoEmpresas, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('superior_logo_lista')
    return render(request, 'superior_logo_confirm_delete.html', {'inscricao': inscricao})

@login_required
def superior_lista(request, id):
    inscricao = get_object_or_404(CursoSuperior, id=id)
    return render(request, 'superior_lista.html', {'inscricao': inscricao})

@login_required
def superior_logo_lista(request):
    inscricoes = LogoEmpresas.objects.all()
    return render(request, 'superior_logo_lista.html', {'inscricoes': inscricoes})

@login_required
def superior_super_lista(request):
    inscricoes = CursoSuper.objects.all()
    return render(request, 'superior_super_lista.html', {'inscricoes': inscricoes})

@login_required
def superior_tec_lista(request):
    inscricoes = CursoTecnico.objects.all()
    return render(request, 'superior_tec_lista.html', {'inscricoes': inscricoes})

@login_required
def superior_pos_lista(request):
    inscricoes = PosGraduacao.objects.all()
    return render(request, 'superior_pos_lista.html', {'inscricoes': inscricoes})

@login_required
def superior_mba_lista(request):
    inscricoes = MBA.objects.all()
    return render(request, 'superior_mba_lista.html', {'inscricoes': inscricoes})

@login_required
def superior_super_novo(request):
    if request.method == 'POST':
        form = CursoSuperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('superior_super_novo')
    else:
        form = CursoSuperForm()
    
    return render(request, 'superior_super_novo.html', {'form': form})

@login_required
def superior_tec_novo(request):
    if request.method == 'POST':
        form = CursoTecnicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('superior_tec_novo')
    else:
        form = CursoTecnicoForm()
    
    return render(request, 'superior_tec_novo.html', {'form': form})

@login_required
def superior_pos_novo(request):
    if request.method == 'POST':
        form = PosGraduacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('superior_pos_novo')
    else:
        form = PosGraduacaoForm()
    
    return render(request, 'superior_pos_novo.html', {'form': form})

@login_required
def superior_mba_novo(request):
    if request.method == 'POST':
        form = MBAForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('superior_mba_novo')
    else:
        form = MBAForm()
    
    return render(request, 'superior_mba_novo.html', {'form': form})

@login_required
def superior_super_update(request, id):
    inscricao = get_object_or_404(CursoSuper, id=id)
    if request.method == 'POST':
        form = CursoSuperForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('superior_super_lista')
    else:
        form = CursoSuperForm(instance=inscricao)
    
    return render(request, 'superior_super_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def superior_tec_update(request, id):
    inscricao = get_object_or_404(CursoTecnico, id=id)
    if request.method == 'POST':
        form = CursoTecnicoForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('superior_tec_lista')
    else:
        form = CursoTecnicoForm(instance=inscricao)
    
    return render(request, 'superior_tec_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def superior_pos_update(request, id):
    inscricao = get_object_or_404(PosGraduacao, id=id)
    if request.method == 'POST':
        form = PosGraduacaoForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('superior_pos_lista')
    else:
        form = PosGraduacaoForm(instance=inscricao)
    
    return render(request, 'superior_pos_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def superior_mba_update(request, id):
    inscricao = get_object_or_404(MBA, id=id)
    if request.method == 'POST':
        form = MBAForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('superior_mba_lista')
    else:
        form = MBAForm(instance=inscricao)
    
    return render(request, 'superior_mba_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def superior_super_delete(request, id):
    inscricao = get_object_or_404(CursoSuper, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('superior_super_lista')
    return render(request, 'superior_super_confirm_delete.html', {'inscricao': inscricao})

@login_required
def superior_tec_delete(request, id):
    inscricao = get_object_or_404(CursoTecnico, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('superior_tec_lista')
    return render(request, 'superior_tec_confirm_delete.html', {'inscricao': inscricao})

@login_required
def superior_mba_delete(request, id):
    inscricao = get_object_or_404(PosGraduacao, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('superior_pos_lista')
    return render(request, 'superior_pos_confirm_delete.html', {'inscricao': inscricao})

@login_required
def superior_pos_delete(request, id):
    inscricao = get_object_or_404(MBA, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('superior_mba_lista')
    return render(request, 'superior_mba_confirm_delete.html', {'inscricao': inscricao})


###### Categoria Profissionalizantes #######
def prof_detalhes(request):
    prof = CursoProf.objects.all()
    logo = LogoEmpresasProf.objects.all()
    pacotes = Pacote.objects.prefetch_related('cursos') 
    turmas = Turma.objects.all()
    data = {
        'prof': prof,
        'logo': logo,
        'pacotes': pacotes,
        'turmas': turmas,
    }
    return render(request, 'prof_detalhes.html', data)

@login_required
def prof_novo(request):
    if request.method == 'POST':
        form = CursoProfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prof_novo')
    else:
        form = CursoProfForm()
    
    return render(request, 'prof_novo.html', {'form': form})

@login_required
def prof_lista(request,id):
    inscricoes = CursoProf.objects.all()
    return render(request, 'prof_lista.html', {'inscricoes': inscricoes})

def prof_logo_novo(request):
    if request.method == 'POST':
        form = LogoEmpresasProfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prof_logo_novo')
    else:
        form = LogoEmpresasProfForm()
    
    return render(request, 'prof_logo_novo.html', {'form': form})

@login_required
def prof_update(request, id):
    inscricao = get_object_or_404(CursoProf, id=id)
    if request.method == 'POST':
        form = CursoProfForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('prof_lista', id=inscricao.id)
    else:
        form = CursoProfForm(instance=inscricao)
    
    return render(request, 'prof_update.html', {'inscricao': inscricao, 'form': form})


@login_required
def prof_logo_lista(request):
    inscricoes = LogoEmpresasProf.objects.all()
    return render(request, 'prof_logo_lista.html', {'inscricoes': inscricoes})

@login_required
def prof_logo_update(request, id):
    inscricao = get_object_or_404(LogoEmpresasProf, id=id)
    if request.method == 'POST':
        form = LogoEmpresasProfForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('prof_logo_lista')
    else:
        form = LogoEmpresasProfForm(instance=inscricao)
    
    return render(request, 'prof_logo_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def prof_logo_delete(request, id):
    inscricao = get_object_or_404(LogoEmpresasProf, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('prof_logo_lista')
    return render(request, 'prof_logo_confirm_delete.html', {'inscricao': inscricao})

def prof_pacote_novo(request):
    if request.method == 'POST':
        form = PacoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prof_pacote_novo')
    else:
        form = PacoteForm()
    
    return render(request, 'prof_pacote_novo.html', {'form': form})

@login_required
def prof_pacote_lista(request):
    inscricoes = Pacote.objects.all()
    return render(request, 'prof_pacote_lista.html', {'inscricoes': inscricoes})

@login_required
def prof_pacote_update(request, id):
    inscricao = get_object_or_404(Pacote, id=id)
    if request.method == 'POST':
        form = PacoteForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('prof_pacote_lista')
    else:
        form = PacoteForm(instance=inscricao)
    
    return render(request, 'prof_pacote_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def prof_pacote_delete(request, id):
    inscricao = get_object_or_404(Pacote, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('prof_pacote_lista')
    return render(request, 'prof_pacote_confirm_delete.html', {'inscricao': inscricao})

def prof_curso_novo(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prof_curso_novo')
    else:
        form = CursoForm()
    
    return render(request, 'prof_curso_novo.html', {'form': form})

@login_required
def prof_curso_lista(request):
    inscricoes = Curso.objects.all()
    return render(request, 'prof_curso_lista.html', {'inscricoes': inscricoes})

@login_required
def prof_curso_update(request, id):
    inscricao = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('prof_curso_lista')
    else:
        form = CursoForm(instance=inscricao)
    
    return render(request, 'prof_curso_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def prof_curso_delete(request, id):
    inscricao = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('prof_curso_lista')
    return render(request, 'prof_curso_confirm_delete.html', {'inscricao': inscricao})

@login_required
def prof_turma_novo(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prof_turma_novo')
    else:
        form = TurmaForm()
    
    return render(request, 'prof_turma_novo.html', {'form': form})

@login_required
def prof_turma_lista(request):
    inscricoes = Turma.objects.all()
    return render(request, 'prof_turma_lista.html', {'inscricoes': inscricoes})

@login_required
def prof_turma_update(request, id):
    inscricao = get_object_or_404(Turma, id=id)
    if request.method == 'POST':
        form = TurmaForm(request.POST, request.FILES, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('prof_turma_lista')
    else:
        form = TurmaForm(instance=inscricao)
    
    return render(request, 'prof_turma_update.html', {'inscricao': inscricao, 'form': form})

@login_required
def prof_turma_delete(request, id):
    inscricao = get_object_or_404(Turma, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('prof_turma_lista')
    return render(request, 'prof_turma_confirm_delete.html', {'inscricao': inscricao})


def cursoson_detalhes(request):
    cursos_lista = CursoAluno.objects.all()
    inscricoes = Inscricao.objects.all()
    digitacao_detalhes = DigitacaoDetalhes.objects.all()

    dados = {
        'cursos_listas': cursos_lista,
        'inscricoes': inscricoes,
        'digitacao_detalhes': digitacao_detalhes,
    }
    return render(request, 'cursoson_detalhes.html', dados)


def cursoson_indivi(request, id):
    curso = get_object_or_404(CursoAluno, id=id)
    inscricao = Inscricao.objects.filter(curso=curso).first()
    licao = Licao.objects.filter(curso=curso).order_by('categoria_ordem', 'ordem')

    if not inscricao:
        licoes = licoes.filter(demo=True)

    categorias = []
    for key, group in groupby(licao, key=lambda x: x.categoria_ordem):
        categorias.append(list(group))

    dados = {
        'curso': curso,
        'inscricao': inscricao,
        'categorias': categorias,
    }
    return render(request, 'cursoson_individual.html', dados)

def cursoson_dig(request):

    dig = get_object_or_404(DigitacaoDetalhes)

    dados = {
        'dig': dig,
    }

    return render(request, 'cursoson_dig.html', dados)