from django.shortcuts import get_object_or_404, render, redirect, render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseBadRequest
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Sum
from django.contrib.staticfiles.storage import staticfiles_storage
import pandas as pd
from django.contrib.staticfiles import finders
import matplotlib.pyplot as plt
import random
from django.template.loader import get_template
from xhtml2pdf import pisa
import io
import os
import json
from itertools import groupby

from .models import Aluno, Curso, Inscricao, Licao, ConclusaoLicao, Digitacao, InscricaoDigitacao, RelatorioDigitacao, ProvaDigitacao, Questao, ItemQuestao, Resposta, DigitacaoDetalhes, Licao
from .forms import AlunoForm, InscricaoForm, LicaoForm, CursoForm, DigitacaoForm, InscricaoDigitacaoForm, ItemQuestaoForm, QuestaoForm, DigitacaoDetalhes


def is_admin(user):
    return user.is_authenticated and user.is_superuser


@login_required
def aluno(request):
    if request.user.is_superuser:
        alunos = Aluno.objects.all()
        alunos_total = alunos.count()
        cursos = Curso.objects.all()
        cursos_total = cursos.count()
        dados = {'alunos_total' : alunos_total,
                'cursos_total' : cursos_total,
                'alunos': alunos,
                }
        return render(request, 'aluno/inic_admin.html', dados)
    else:
        aluno = Aluno.objects.get(user=request.user)
    
        if not aluno.cadastro_completo:
            return redirect('aluno_aluno_update', id=aluno.id)  
        else:      
            aluno = Aluno.objects.get(user=request.user)  # Filtra o aluno atualmente autenticado
            inscricoes = Inscricao.objects.filter(aluno=request.user)
            num_inscricoes = inscricoes.count()
            inscricoesDigitacao = InscricaoDigitacao.objects.filter(aluno=request.user)
            digitacao = Digitacao.objects.all()
            digitacao_licao_total = digitacao.count()


            try:
                inscricao_digitacao = InscricaoDigitacao.objects.get(aluno=request.user)
                licao_atual = inscricao_digitacao.licao_atual
                digitacao_porcento = float((licao_atual - 1) / digitacao.count() * 100) if digitacao.count() > 0 else 0
            except InscricaoDigitacao.DoesNotExist:
                inscricao_digitacao = None
                licao_atual = 0
                digitacao_porcento = 0

            dados_cursos = []
            for inscricao in inscricoes:
                curso = inscricao.curso
                licoes_feitas = ConclusaoLicao.objects.filter(aluno=request.user, curso=curso, status='concluido')
                licoes_total = curso.licao_set.count()
                licoes_porcento = float(licoes_feitas.count() / licoes_total * 100) if licoes_total > 0 else 0

                dados_cursos.append({
                    'curso': curso,
                    'licoes_feitas': licoes_feitas,
                    'licoes_total': licoes_total,
                    'licoes_porcento': licoes_porcento,

                })

            dados = {
                'aluno': aluno,
                'num_inscricoes': num_inscricoes,
                'dados_cursos': dados_cursos,
                'inscricoesDigitacao' : inscricoesDigitacao,
                'digitacao': digitacao,
                'digitacao_licao_total': digitacao_licao_total,
                'licao_atual': request.session.get('licao_atual'),  # Adicione esta linha
                'digitacao_porcento': digitacao_porcento,
            }
            
            return render(request, 'aluno/inic_aluno.html', dados)


@login_required
def minhaconta(request):
    aluno = Aluno.objects.get(user=request.user)  # Filtra o aluno atualmente autenticado
    inscricoes = Inscricao.objects.filter(aluno=request.user)
    inscricoesDigitacao = InscricaoDigitacao.objects.filter(aluno=request.user)
    digitacao = Digitacao.objects.all()
    digitacao_licao_total = digitacao.count()
    try:
        inscricao_digitacao = InscricaoDigitacao.objects.get(aluno=request.user)
        licao_atual = inscricao_digitacao.licao_atual
        digitacao_porcento = float(licao_atual / digitacao.count() * 100) if digitacao.count() > 0 else 0
    except InscricaoDigitacao.DoesNotExist:
        inscricao_digitacao = None
        licao_atual = 0
        digitacao_porcento = 0

    # Filtrar o objeto ProvaDigitacao com base no usuário logado
    prova_digitacao = ProvaDigitacao.objects.filter(aluno=request.user).first()
    # Verificar se a prova de digitação existe para o aluno logado
    if prova_digitacao:
        # Capturar a variável nota do objeto ProvaDigitacao
        nota = prova_digitacao.nota
    else:
        nota = None

    dados_cursos = []
    for inscricao in inscricoes:
        curso = inscricao.curso
        licoes_feitas = ConclusaoLicao.objects.filter(aluno=request.user, curso=curso, status='concluido')
        licoes_total = curso.licao_set.count()
        licoes_porcento = float(licoes_feitas.count() / licoes_total * 100) if licoes_total > 0 else 0


        dados_cursos.append({
            'curso': curso,
            'licoes_feitas': licoes_feitas,
            'licoes_total': licoes_total,
            'licoes_porcento': licoes_porcento,

        })
    
    resposta = Resposta.objects.filter(aluno=aluno).first()
    nota_resposta = resposta.nota if resposta else None

    dados = {
        'aluno': aluno,
        'dados_cursos': dados_cursos,
        'inscricoesDigitacao' : inscricoesDigitacao,
        'digitacao': digitacao,
        'digitacao_licao_total': digitacao_licao_total,
        'licao_atual': request.session.get('licao_atual'),  # Adicione esta linha
        'digitacao_porcento': digitacao_porcento,
        'nota': nota,
        'nota_resposta': nota_resposta,  # Adicione esta linha com o nome atualizado
    }
    return render(request, 'aluno/inic_minha_conta.html', dados)


@permission_required('aluno.administrador', login_url='/login/')
def administrador(request):
    # Código para exibir a página para usuários com permissão
    return render(request, 'aluno/inic_admin.html')


@login_required
def pagina_inicial(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('adminstrador')
        else:
            aluno = Aluno.objects.get(user=request.user)
            if not aluno.cadastro_completo:
                return redirect('aluno_aluno_update', id=aluno.id)
            return redirect('aluno')
    else:
        return redirect('/login/')

        
@login_required
def lista_alunos(request):
    alunos_lista = Aluno.objects.all()
    search = request.GET.get('search')
    if search:
        alunos = Aluno.objects.filter(user__username__icontains=search)
    else:
        paginator = Paginator(alunos_lista, 15)
        page = request.GET.get('page')
        alunos = paginator.get_page(page)


    users = User.objects.all()
    alunos_total = alunos_lista.count()
    form = AlunoForm()
    data = {
        'alunos': alunos,
        'form': form,
        'users': users,
        'alunos_total' : alunos_total,
        }
    # adiciona verificação para o campo foto
    for aluno in alunos:
        if not aluno.foto:
            aluno.foto = 'media/aluno/foto/default.png'
            aluno.save()
    return render(request, 'aluno/lista_alunos.html', data)

@login_required
@user_passes_test(is_admin)
def aluno_novo(request):
    #if request.user.has_perm('aluno.add_aluno'):
    #    return HttpResponse('Não autorizado')
    #elif not request.user.is_superuser:
    #    return HttpResponse('Não e super usuário')
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('aluno_alunos')


@login_required
def aluno_update(request, id):
    data = {}
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(request.POST or None, request.FILES or None, instance=aluno)  # Importante: Adicione request.FILES aqui
    data['aluno'] = aluno
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            # Salvar o novo formulário
            aluno = form.save(commit=False)  # Salva sem persistir no banco ainda
            
            # Verifica se uma nova foto foi carregada
            if 'foto' in request.FILES:
                # Se uma nova foto foi carregada, exclua a antiga se existir
                if aluno.foto:
                    default_storage.delete(aluno.foto.path)

                # Salva a nova foto
                aluno.foto = request.FILES['foto']

            aluno.cadastro_completo = True  # Marcar o cadastro como completo
            aluno.save()  # Salva no banco
            return redirect('/')  # Redireciona após o salvamento
    return render(request, 'aluno/update_aluno.html', data)




@login_required
@user_passes_test(is_admin)
def aluno_delete(request, id):
    aluno = Aluno.objects.get(id=id)
    user = User.objects.get(id=id)
    if request.method == 'POST':
        aluno.delete()
        user.delete()
        return redirect('aluno_alunos')
    else:
        return render(request, 'aluno/delete_confirm.html', {'obj': aluno})


@login_required
@user_passes_test(is_admin)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user_id)
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'aluno/edit_user.html', {'form': form})



#def cursos(request):
#    cursos = Curso.objects.all()
#    return render(request, 'cursos/cursos.html', {'cursos': cursos})

@login_required
@user_passes_test(is_admin)
def lista_cursos(request):
    #cursos = Curso.objects.all()
    cursos_lista = Curso.objects.all()

    paginator = Paginator(cursos_lista, 15)
    page = request.GET.get('page')
    cursos = paginator.get_page(page)

    curso_total = cursos_lista.count()
    dados = {'cursos': cursos,
            'curso_total' : curso_total,
            }
    return render(request, 'aluno/lista_cursos.html', dados)


@login_required
@user_passes_test(is_admin)
def curso_novo(request):
    
    if request.method == 'POST':
        form = CursoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'aluno/novo_curso.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def curso_update(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            # Salvar o novo arquivo de imagem se uma nova imagem foi enviada
            nova_imagem = request.FILES.get('imagem')
            if nova_imagem is not None:
                # Excluir a imagem antiga, se existir
                if curso.imagem:
                    default_storage.delete(curso.imagem.path)
                curso.imagem.save(nova_imagem.name, ContentFile(nova_imagem.read()))

            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'aluno/update_curso.html', {'form': form, 'curso': curso})



@login_required
@user_passes_test(is_admin)
def curso_delete(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')
    else:
        return render(request, 'aluno/delete_confirm.html', {'obj': curso})


@login_required
def lista_Licao(request, id):
    licao = get_object_or_404(Licao, id=id)
    form = LicaoForm()
    
    # Obter a lição atual
    licoes = Licao.objects.filter(curso=licao.curso).order_by('categoria_ordem', 'ordem')
    
    # Encontrar o índice da lição atual
    index = list(licoes).index(licao)

    # Definir a lição anterior e a próxima licao_anterior
    licao_anterior = licoes[index - 1] if index > 0 else None
    próxima_licao = licoes[index + 1] if index < len(licoes) - 1 else None

    # Atualizar status da lição anterior se necessário
    if 'update_status' in request.GET and licao_anterior:
        conclusao_licao, created = ConclusaoLicao.objects.get_or_create(
            aluno=request.user,
            licao=licao_anterior,
            curso=licao_anterior.curso
        )

        # Testar se o status está como "fazer" ou se a lição ainda não foi concluída
        if conclusao_licao.status == 'fazer' or created:
            conclusao_licao.status = 'concluido'
            conclusao_licao.save()


    data = {
        'licao': licao,
        'form': form,
        'licao_anterior': licao_anterior,
        'proxima_licao': próxima_licao,
    }
    return render(request, 'aluno/detalhes_licao.html', data)


@login_required
@user_passes_test(is_admin)
def inscrever_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    inscricao = Inscricao(usuario=request.user, curso=curso)
    inscricao.save()
    return redirect('aluno/lista_licoes.html', curso_id=curso.id)


@login_required
@user_passes_test(is_admin)
def lista_inscricoes(request):
    inscricoes = Inscricao.objects.filter(aluno=request.user)
    curso = Curso.objects.filter(id__in=inscricoes.values('curso'))

    inscricoesDigitacao = InscricaoDigitacao.objects.filter(aluno=request.user)
    digitacao = Digitacao.objects.filter(id__in=inscricoesDigitacao.values('digitacao'))
    inscricao_digitacao = InscricaoDigitacao.objects.get(aluno=request.user)
    licao_atual = inscricao_digitacao.licao_atual

    form = InscricaoForm()
    data = {
            'inscricoes': inscricoes,
            'inscricoesDigitacao': inscricoesDigitacao,
            'curso': curso,
            'digitacao': digitacao,
            'form': form,
            'licao_atual': licao_atual,
            }
    return render(request, 'aluno/lista_inscricoes.html', data)


@login_required
@user_passes_test(is_admin)
def inscricao_update(request, id):
    data = {}
    inscricao = Inscricao.objects.get(id=id)
    form = InscricaoForm(request.POST or None, instance=inscricao)
    data['inscricao'] = inscricao
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_inscricao')
    else:
        return render(request, 'aluno/update_inscricao.html', data)


@login_required
@user_passes_test(is_admin)
def inscricao_delete(request, id):
    inscricao = Inscricao.objects.get(id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('lista_inscricao')
    else:
        return render(request, 'aluno/delete_confirm.html', {'obj': inscricao})


@login_required
def lista_inscricao(request):
    inscricoes_lista = Inscricao.objects.all()
    search = request.GET.get('search')
    if search:

        inscricoes = Inscricao.objects.filter(aluno__username__icontains=search)
    else:
        paginator = Paginator(inscricoes_lista, 15)
        page = request.GET.get('page')
        inscricoes = paginator.get_page(page)

    num_incricoes = inscricoes_lista.count()
    dados ={'inscricoes': inscricoes,
            'num_incricoes': num_incricoes
            }
    return render(request, 'aluno/lista_inscricao.html', dados)


@login_required
def curso_detalhe(request, id):
    curso = get_object_or_404(Curso, id=id)
    conclusaoLicao = ConclusaoLicao.objects.all()
    
    licao = Licao.objects.filter(curso=curso).order_by('categoria_ordem', 'ordem')

    categorias = []
    for key, group in groupby(licao, key=lambda x: x.categoria_ordem):
        categorias.append(list(group))
    aluno = request.user

    licoes_feitas = ConclusaoLicao.objects.filter(aluno=aluno, curso=curso, status='concluido')
    licoes_porcento = float(licoes_feitas.count() / licao.count() * 100) if licao.count() > 0 else 0
    conclusaoLicao = ConclusaoLicao.objects.filter(aluno=aluno, curso=curso, status='concluido')
    licao_concluida = [conclusao.licao for conclusao in conclusaoLicao]

    porcento = int(licoes_porcento)
    
    # Armazenar a porcentagem na sessão
    request.session['porcento'] = porcento

    aluno = request.user.aluno
    curso = get_object_or_404(Curso, pk=id)
    respostas = Resposta.objects.filter(aluno=aluno, curso=curso)
    nota = respostas.aggregate(nota_total=Sum('nota')).get('nota_total', 0)

    categorias_concluidas = {}
    for categoria in categorias:
        todas_concluidas = all(licao in licao_concluida for licao in categoria)
        categorias_concluidas[categoria[0].categoria] = todas_concluidas


    categoria_licao = request.session.get('categoria_licao', 1)

    data = {
        'curso': curso,
        'licao': licao,
        'licao_total': licao.count(),
        'licao_feitas': licoes_feitas.count(),
        'licao_porcento': licoes_porcento,
        'porcento': porcento,
        'categorias': categorias,
        'categorias_concluidas': categorias_concluidas,
        'conclusaoLicao': conclusaoLicao,
        'aluno': aluno,
        'licao_concluida': licao_concluida,
        'nota': nota,
        'selo': curso.selo,
        'selo_fundo': curso.selo_cinza,
        'selo_prova': curso.selo_prova,  # Adicione esta linha para passar a variável 'selo'
        'selo_prova_fundo': curso.selo_prova_cinza,
        'selo_max': curso.selo_max,
        'selo_max_fundo': curso.selo_cinza_max,
        'categoria_licao': categoria_licao,
    }
    return render(request, 'aluno/curso_detalhe.html', data)



@login_required
def changeStatus(request, id, categoria_licao):
    licao = get_object_or_404(Licao, pk=id)
    aluno = request.user

    try:
        conclusao_licao = ConclusaoLicao.objects.get(licao=licao, aluno=aluno)
        if conclusao_licao.status == 'fazer' or conclusao_licao.status is None:
            conclusao_licao.status = 'concluido'
        else:
            conclusao_licao.status = 'fazer'
        conclusao_licao.save()
    except ConclusaoLicao.DoesNotExist:
        status = 'fazer' if request.POST.get('status') == 'fazer' else 'concluido'
        conclusao_licao = ConclusaoLicao.objects.create(
            aluno=aluno,
            licao=licao,
            curso=licao.curso,
            status=status
        )

    # Atualize o valor de categoria_licao na sessão
    request.session['categoria_licao'] = categoria_licao

    # Retorne o novo status como JSON
    return JsonResponse({'status': conclusao_licao.status})


@login_required
def licao_detalhe(request, id):
    curso = get_object_or_404(Curso, id=id)
    licao = Licao.objects.filter(curso=curso).order_by('categoria_ordem', 'ordem')

    categorias = []
    for key, group in groupby(licao, key=lambda x: x.categoria_ordem):
        categorias.append(list(group))

    data = {
        'curso': curso,
        'categorias': categorias,
        'licao_total': licao.count(),
    }
    return render(request, 'aluno/licao_detalhe.html', data)


@login_required
@user_passes_test(is_admin)
def inscricao_novo(request):
    form = InscricaoForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect('lista_inscricao')
    else:
        return render(request, 'aluno/novo_inscricao.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def licao_novo(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    form = LicaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        licao = form.save(commit=False)
        licao.curso = curso
        licao.save()
        #return redirect('/licao-lista/', curso_id=curso_id)
        url = '/licao-lista/{}'.format(curso_id)
        return redirect(url)
    return render(request, 'aluno/novo_licao.html', {'form': form, 'curso': curso})
    

@login_required
@user_passes_test(is_admin)
def licao_update(request, id):
    data = {}
    licao = Licao.objects.get(id=id)
    form = LicaoForm(request.POST or None, instance=licao)
    data['licao'] = licao
    data['form'] = form
    curso_id = licao.curso.id
    if request.method == 'POST':
        if form.is_valid():
            if licao.botao:
                default_storage.delete(licao.botao.path)

            botao = request.FILES.get('botao')
            if botao:
                licao.botao.save(botao.name, ContentFile(botao.read()))

            form.save()
            url = '/licao-lista/{}'.format(curso_id)
            return redirect(url)
    else:
        return render(request, 'aluno/update_licao.html', data)


@login_required
@user_passes_test(is_admin)
def licao_delete(request, id):
    licao = Licao.objects.get(id=id)
    curso_id = licao.curso.id
    if request.method == 'POST':
        licao.delete()
        url = '/licao-lista/{}'.format(curso_id)
        return redirect(url)
    else:
        return render(request, 'aluno/delete_confirm.html', {'obj': licao})


@login_required
def download_licao(request, licao_id):
    licao = get_object_or_404(Licao, id=licao_id)
    if licao.botao:
        file_path = licao.botao.path
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + licao.botao.name
            return response
    else:
        return HttpResponse("Arquivo não encontrado.")    

@login_required
@user_passes_test(is_admin)
def lista_digitacao(request):
    digitacao_lista = Digitacao.objects.all()
    digitacao_detalhes = DigitacaoDetalhes.objects.all()

    paginator = Paginator(digitacao_lista, 15)
    page = request.GET.get('page')
    digitacao = paginator.get_page(page)

    digitacao_total = digitacao_lista.count()
    dados = {
        'digitacao': digitacao,
        'digitacao_total': digitacao_total,
        'digitacao_detalhes': digitacao_detalhes,
    }
    return render(request, 'aluno/lista_digitacao.html', dados)


@login_required
@user_passes_test(is_admin)
def digitacao_novo(request):
    
    if request.method == 'POST':
        form = DigitacaoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            inscricoes = InscricaoDigitacao.objects.filter(aluno=request.user)
            return redirect('lista_digitacao')
    else:
        form = DigitacaoForm()
    return render(request, 'aluno/novo_digitacao.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def digitacao_update(request, id):
    data = {}
    digitacao = Digitacao.objects.get(id=id)
    form = DigitacaoForm(request.POST or None, instance=digitacao)
    data['digitacao'] = digitacao
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_digitacao')
    else:
        return render(request, 'aluno/update_digitacao.html', data)


@login_required
@user_passes_test(is_admin)
def digitacao_delete(request, id):
    digitacao = Digitacao.objects.get(id=id)
    if request.method == 'POST':
        digitacao.delete()
        return redirect('lista_digitacao')
    else:
        return render(request, 'aluno/delete_confirm.html', {'obj': digitacao})


@login_required
@user_passes_test(is_admin)
def lista_inscricaodigitacao(request):
    inscricoes = InscricaoDigitacao.objects.all()
    digitacao = Digitacao.objects.filter(id__in=inscricoes.values('digitacao'))
    num_incricoes = inscricoes.count()
    form = InscricaoDigitacaoForm()
    data = {
            'inscricoes': inscricoes,
            'digitacao': digitacao,
            'num_incricoes': num_incricoes,
            'form': form,
            }
    return render(request, 'aluno/lista_inscricaodigitacao.html', data)


@login_required
@user_passes_test(is_admin)
def inscricaodigitacao_novo(request):
    
    if request.method == 'POST':
        form = InscricaoDigitacaoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_inscricaodigitacao')
    else:
        form = InscricaoDigitacaoForm()
    return render(request, 'aluno/novo_inscricaodigitacao.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def inscricaodigitacao_update(request, id):
    data = {}
    digitacao = InscricaoDigitacao.objects.get(id=id)
    form = InscricaoDigitacaoForm(request.POST or None, instance=digitacao)
    data['digitacao'] = digitacao
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_inscricaodigitacao')
    else:
        return render(request, 'aluno/update_inscricaodigitacao.html', data)


@login_required
@user_passes_test(is_admin)
def inscricaodigitacao_delete(request, id):
    digitacao = InscricaoDigitacao.objects.get(id=id)
    if request.method == 'POST':
        digitacao.delete()
        return redirect('lista_inscricaodigitacao')
    else:
        return render(request, 'aluno/delete_confirm.html', {'obj': digitacao})


@login_required
def cursodigitacao_detalhe(request, id):
    inscricoes = InscricaoDigitacao.objects.filter(aluno=request.user)
    digitacao = Digitacao.objects.filter(ordem__in=inscricoes.values('licao_atual'))
    form = InscricaoDigitacaoForm()
    num_licoes = digitacao.count()
    total_licoes = Digitacao.objects.all().count()

    licao_atual = id
    request.session['licao_atual'] = licao_atual
    proxima_licao = digitacao.filter(ordem__gt=licao_atual).first()
    todas_licoes_concluidas = licao_atual >= num_licoes

    data = {
            'digitacao': digitacao,
            'num_licoes': num_licoes,
            'inscricoes': inscricoes,
            'proxima_licao': proxima_licao,
            'total_licoes': total_licoes,
            'todas_licoes_concluidas': todas_licoes_concluidas,
            'form': form,
            'licao_atual': licao_atual,  # Adicione esta linha
            }
    return render(request, 'aluno/lista_inscricao_digitacao.html', data)


@login_required
def cursodigitacao_next(request, id):
    inscricao = InscricaoDigitacao.objects.get(id=id)
    inscricao.licao_atual += 1

    if inscricao.data_acesso.date() != timezone.now().date():
        # A data de acesso é diferente da data atual
        inscricao.contador_licao = 1  # Zerar contador_licao
        inscricao.data_acesso = timezone.now()  # Definir data_acesso como a data atual
    else:
        # A data de acesso é a mesma da data atual
        inscricao.contador_licao += 1  # Incrementar contador_licao

    inscricao.save()
    return redirect('cursodigitacao_detalhe', id=inscricao.id)


@csrf_exempt
def relatorioDigitacao(request):
    if request.method == 'POST':
        toques = float(request.POST.get('toques'))
        acertos = float(request.POST.get('acertos'))
        erros = float(request.POST.get('erros'))
        licao_atual = request.POST.get('licao_atual')
        tempo = float(request.POST.get('tempo'))
        
        # Crie uma instância de RelatorioDigitacao e salve no banco de dados
        relatorio = RelatorioDigitacao(
            aluno=request.user,
            licao_atual=licao_atual,
            toques=toques,
            acertos=acertos,
            erros=erros,
            tempo=tempo,
        )
        relatorio.save()
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

def obter_relatorioDigitacao(request):
    # Obtenha os relatórios de digitação do banco de dados
    relatorios = RelatorioDigitacao.objects.filter(aluno=request.user)

    # Crie um DataFrame com os dados relevantes dos relatórios
    dados_relatorio = pd.DataFrame(list(relatorios.values()))

    # Converter as colunas para tipos de dados numéricos
    dados_relatorio['toques'] = dados_relatorio['toques'].astype(float)
    dados_relatorio['acertos'] = dados_relatorio['acertos'].astype(float)
    dados_relatorio['erros'] = dados_relatorio['erros'].astype(float)
    dados_relatorio['tempo'] = dados_relatorio['tempo'].astype(float)

    # Agrupe os dados por lição e calcule a média dos toques, acertos e erros
    dados_agrupados = dados_relatorio.groupby('licao_atual').mean()

    # Crie o gráfico comparativo de linhas
    plt.plot(dados_agrupados.index, dados_agrupados['toques'], label='Toques')
    plt.plot(dados_agrupados.index, dados_agrupados['acertos'], label='Acertos')
    plt.plot(dados_agrupados.index, dados_agrupados['erros'], label='Erros')
    plt.plot(dados_agrupados.index, dados_agrupados['tempo'], label='Tempo')

    # Adicione rótulos e legendas ao gráfico
    plt.xlabel('Lição')
    plt.ylabel('Quantidade')
    plt.title('Comparativo de Toques, Acertos e Erros por Lição')
    plt.legend()

    # Calcule as médias das colunas
    tempo_media = dados_agrupados['tempo'].mean()
    toques_media = dados_agrupados['toques'].mean()
    acertos_media = dados_agrupados['acertos'].mean()
    erros_media = dados_agrupados['erros'].mean()

    # Renderize o template e passe os dados para o contexto
    return render(request, 'aluno/lista_digitacao_relatorio.html', {
        'relatorios': dados_relatorio,
        'licoes': dados_agrupados.index.tolist(),
        'toques': dados_agrupados['toques'].tolist(),
        'acertos': dados_agrupados['acertos'].tolist(),
        'erros': dados_agrupados['erros'].tolist(),
        'tempo': dados_agrupados['tempo'].tolist(),
        'tempo_media': tempo_media,
        'toques_media': toques_media,
        'acertos_media': acertos_media,
        'erros_media': erros_media
    })

@login_required
def provasdigitacao(request, id):
    provas = ProvaDigitacao.objects.filter(aluno=request.user)

    data = {
        'provas': provas,
    }
    return render(request, 'aluno/prova_digitacao.html', data)


@csrf_exempt
def criar_prova_digitacao(request):
    if request.method == 'POST':
        # Obter o corpo da solicitação JSON
        data = json.loads(request.body)
        
        # Obter os valores necessários
        toques_por_minuto = data.get('toques_por_minuto')
        nota = data.get('nota')
        tempo_decorrido = data.get('tempo_decorrido')
        erros = data.get('erros')
        data_conclusao = timezone.now()


        # Cria um novo objeto ProvaDigitacao
        prova_digitacao = ProvaDigitacao(
            aluno=request.user,
            toques=toques_por_minuto,
            nota=nota,
            tempo=tempo_decorrido,
            erros=erros,
            data_conclusao=data_conclusao
        )
        prova_digitacao.save()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
def rankindigitacao(request):
    rank = ProvaDigitacao.objects.order_by('-toques', 'tempo', 'erros').select_related('aluno')
    foto = Aluno.objects.all()
    dados = {
        'rank': rank,
        'foto': foto,
    }
    return render(request, 'aluno/rank_digitacao.html', dados)


@login_required
def prova(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    questoes = list(Questao.objects.filter(curso=curso))

    for questao in questoes:
        questao.itens_embaralhados = random.sample(list(questao.itemquestao_set.all()), k=len(questao.itemquestao_set.all()))

    random.shuffle(questoes)  # Embaralhar as questões

    return render(request, 'aluno/prova.html', {'curso': curso, 'questoes': questoes})


def processar_respostas(request, curso_id):
    if request.method == 'POST':
        aluno = request.user.aluno
        curso = get_object_or_404(Curso, pk=curso_id)
        questoes = Questao.objects.filter(curso=curso)
        respostas = []
        questoes_nao_respondidas = False

        for questao in questoes:
            item_respondido_id = request.POST.get(f'questao_{questao.id}', None)
            if item_respondido_id:
                item_respondido = get_object_or_404(ItemQuestao, pk=item_respondido_id)
                respostas.append({'questao': questao, 'item_respondido': item_respondido})
            else:
                messages.error(request, 'Pelo menos uma questão não foi respondida.')
                questoes_nao_respondidas = True

        if len(respostas) != len(questoes):
            messages.error(request, 'Selecione pelo menos uma resposta para concluir a prova.')
            questoes_nao_respondidas = True

        if questoes_nao_respondidas:
            return render(request, 'aluno/prova.html', {'curso': curso, 'questoes': questoes, 'questoes_nao_respondidas': questoes_nao_respondidas})

        total_questoes = len(questoes)
        numero_acertos = 0

        for resposta in respostas:
            questao = resposta['questao']
            item_respondido = resposta['item_respondido']

            # Lógica para comparar a resposta selecionada com a resposta correta e incrementar o número de acertos
            if item_respondido.correto:
                numero_acertos += 1

        #pontuacao = total_questoes - (total_questoes - numero_acertos)
        pontuacao = numero_acertos * 10 / total_questoes
        passou_prova = pontuacao >= 6

        # Atualize a nota do aluno
        Resposta.objects.update_or_create(aluno=aluno, curso=curso, defaults={'nota': pontuacao})

        return redirect('resultado_prova', curso_id=curso_id)

    return render(request, 'aluno/prova.html', {'curso': curso, 'questoes': questoes})

@login_required
def resultado_prova(request, curso_id):
    aluno = request.user.aluno
    curso = get_object_or_404(Curso, pk=curso_id)
    respostas = Resposta.objects.filter(aluno=aluno, curso=curso)
    nota = respostas.aggregate(nota_total=Sum('nota')).get('nota_total', 0)

    dados = {
        'curso': curso,
        'respostas': respostas,
        'nota': nota,
        'selo_prova': curso.selo_prova,  # Adicione esta linha para passar a variável 'selo'
        'selo_max': curso.selo_max,
    }


    return render(request, 'aluno/resultado_prova.html', dados)

@login_required
def questoes_detalhe(request, id):
    curso = get_object_or_404(Curso, id=id)
    questoes = Questao.objects.filter(curso=curso)

    data = {
        'curso': curso,
        'questoes': questoes,
    }
    return render(request, 'aluno/lista_questoes.html', data)


def itens_detalhe(request, curso_id, questao_id):
    questao = get_object_or_404(Questao, id=questao_id)
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = ItemQuestaoForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.questao = questao
            item.save()
            return redirect('questoes_detalhe', id=curso_id)  # Redireciona para 'questoes_detalhe' com o ID do curso
    else:
        form = ItemQuestaoForm(initial={'questao': questao})

    return render(request, 'aluno/lista_prova_itens.html', {'form': form, 'curso': curso})


def excluir_item(request, item_id):
    item = get_object_or_404(ItemQuestao, id=item_id)
    questao_id = item.questao.id
    curso_id = item.questao.curso.id  # Obtenha o ID do curso relacionado à questão
    item.delete()
    return redirect('questoes_detalhe', id=curso_id)  # Redireciona para 'questoes_detalhe' com o ID do curso


def editar_item(request, item_id):
    item = get_object_or_404(ItemQuestao, id=item_id)

    if request.method == 'POST':
        form = ItemQuestaoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('questoes_detalhe', id=item.questao.curso.id)
    else:
        form = ItemQuestaoForm(instance=item)

    return render(request, 'aluno/editar_item.html', {'form': form, 'item': item})


def criar_questao(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = QuestaoForm(request.POST)
        if form.is_valid():
            questao = form.save(commit=False)
            questao.curso = curso
            questao.save()
            return redirect('questoes_detalhe', id=curso_id)
    else:
        form = QuestaoForm(initial={'curso': curso})

    return render(request, 'aluno/criar_questao.html', {'form': form, 'curso': curso})


def editar_questao(request, questao_id):
    questao = get_object_or_404(Questao, id=questao_id)

    if request.method == 'POST':
        form = QuestaoForm(request.POST, instance=questao)
        if form.is_valid():
            form.save()
            return redirect('questoes_detalhe', id=questao.curso.id)
    else:
        form = QuestaoForm(instance=questao)

    return render(request, 'aluno/editar_questao.html', {'form': form, 'questao': questao})


def excluir_questao(request, questao_id):
    questao = get_object_or_404(Questao, id=questao_id)
    
    # Verifique se a questão tem itens relacionados
    if questao.itemquestao_set.exists():
        return HttpResponseBadRequest("Esta questão possui itens associados e não pode ser excluída.")
    
    curso_id = questao.curso.id  # Obtenha o ID do curso relacionado à questão
    questao.delete()
    return redirect('questoes_detalhe', id=curso_id)

@login_required
def gerar_certificado(request, curso_id):
    aluno = request.user.aluno
    curso = get_object_or_404(Curso, id=curso_id)
    

    # Renderiza o certificado em HTML
    template = get_template('aluno/certificado.html')
    context = {'aluno': aluno, 'curso': curso}
    html = template.render(context)

    # Define as opções de configuração
    options = {
        'encoding': 'UTF-8',
        'show_content_wait': True,
    }

    # Converte o HTML para PDF com orientação paisagem
    pdf_file = io.BytesIO()
    pisa.CreatePDF(html, dest=pdf_file, link_callback=None, **options)

    # Retorna o PDF como resposta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="certificado.pdf"'
    response.write(pdf_file.getvalue())

    return response

def certificadoteste(request, curso_id):
    aluno = Aluno.objects.get(user=request.user)
    curso = get_object_or_404(Curso, id=curso_id)

    return render(request, 'aluno/certificado.html', { 'aluno': aluno, 'curso': curso})



def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Normalmente /static/
        sRoot = settings.STATIC_ROOT  # Normalmente /path/to/static/
        mUrl = settings.MEDIA_URL    # Normalmente /media/
        mRoot = settings.MEDIA_ROOT  # Normalmente /path/to/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # Verificar se o arquivo realmente existe
    if not os.path.isfile(path):
        raise RuntimeError(f'Arquivo não encontrado: {path}')
    return path


# View para gerar o PDF
def render_pdf_view(request,curso_id):
    # Carregar o template
    template = get_template('aluno/certificado.html')

    aluno = Aluno.objects.get(user=request.user)
    curso = get_object_or_404(Curso, id=curso_id)
    data_prova = get_object_or_404(Resposta, id=curso_id)
    
    # Gerar a URL completa para a imagem estática
    caminho_imagem = request.build_absolute_uri(staticfiles_storage.url('media/infox/certificado/certificado_fundo.png'))

    # Gerar a URL completa para a fonte
    caminho_fonte = request.build_absolute_uri(staticfiles_storage.url('media/infox/certificado/al.ttf'))

    # Configurar o contexto com dados
    context = {

        'aluno': aluno,
        'curso': curso,
        'data_prova':data_prova,
        'caminho_imagem': caminho_imagem,
        'caminho_fonte': caminho_fonte,
    }

    # Renderizar o template em HTML
    html = template.render(context)

    # Criar a resposta do Django
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="certificado.pdf"'

    # Gerar o PDF com xhtml2pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback  # Aqui chamamos link_callback
    )

    # Verificar se houve erros
    if pisa_status.err:
        return HttpResponse(f'Erro ao gerar o PDF: {pisa_status.err}', status=500)

    return response


@login_required
def render_pdf_digitacao_view(request):
    # Carregar o template de certificado de digitação
    template = get_template('aluno/certificado_digitacao.html')

    aluno = Aluno.objects.get(user=request.user)
    # Filtrar as provas de digitação do aluno
    provas = ProvaDigitacao.objects.filter(aluno=request.user)

    # Gerar a URL completa para a imagem estática do certificado de digitação
    caminho_imagem = request.build_absolute_uri(staticfiles_storage.url('media/infox/certificado/certificado_fundo.png'))

    # Gerar a URL completa para a fonte utilizada no certificado
    caminho_fonte = request.build_absolute_uri(staticfiles_storage.url('media/infox/certificado/al.ttf'))

    # Configurar o contexto com as informações necessárias para o template
    context = {
        'aluno': aluno,
        'provas': provas,
        'caminho_imagem': caminho_imagem,
        'caminho_fonte': caminho_fonte,
    }

    # Renderizar o template HTML
    html = template.render(context)

    # Criar a resposta do Django como um PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="certificado_digitacao.pdf"'

    # Gerar o PDF com xhtml2pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback
    )

    # Verificar se houve erros na geração do PDF
    if pisa_status.err:
        return HttpResponse(f'Erro ao gerar o PDF: {pisa_status.err}', status=500)

    return response

@login_required
@csrf_exempt
def marcar_tour_completo(request):
    if request.method == "POST":
        aluno = request.user.aluno
        aluno.tour_completo = False
        aluno.save()
        return JsonResponse({'status': 'success'})
    else:
        print('Método não permitido')  # Adicione este log
        return JsonResponse({'status': 'error', 'message': 'Método não permitido.'})

@csrf_exempt  # Para permitir requisições AJAX com POST
@login_required
def toggle_tour_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tour_completo = data.get('tour_completo', False)  # Pega o valor enviado do checkbox
        
        aluno = Aluno.objects.get(user=request.user)  # Obtém o aluno autenticado
        aluno.tour_completo = tour_completo  # Atualiza o campo tour_completo
        aluno.save()  # Salva as mudanças no banco de dados
        
        return JsonResponse({'success': True})  # Retorna sucesso

    return JsonResponse({'success': False}, status=400)  # Retorna erro se não for POST

@login_required
@csrf_exempt  # Se você não puder garantir o CSRF
def marcar_tour_completoDig(request):
    if request.method == "POST":
        aluno = request.user.aluno
        aluno.tour_dig_completo = False
        aluno.save()
        return JsonResponse({'status': 'success'})
    else:
        print('Método não permitido')  # Adicione este log
        return JsonResponse({'status': 'error', 'message': 'Método não permitido.'})
    
@csrf_exempt
@login_required
def toggle_tour_status_dig(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tour_completo_dig = data.get('tour_dig_completo', False)  # Pega o valor enviado do checkbox
        
        aluno = Aluno.objects.get(user=request.user)  # Obtém o aluno autenticado
        aluno.tour_dig_completo = tour_completo_dig  # Atualiza o campo tour_completo
        aluno.save()  # Salva as mudanças no banco de dados
        
        return JsonResponse({'success': True})  # Retorna sucesso

    return JsonResponse({'success': False}, status=400)  # Retorna erro se não for POST