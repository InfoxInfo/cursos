from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from aluno.models import Curso as CursoAluno, Curso, DigitacaoDetalhes
from django.contrib import messages


def Pagar(request):
    return render(request, 'pedido/pedido.html')

def adicionar_ao_carrinho(request, id):
    curso = get_object_or_404(Curso, id=id)
    carrinho = request.session.get('carrinho', {})

    if str(id) in carrinho:
        carrinho[str(id)] += 1
    else:
        carrinho[str(id)] = 1

    request.session['carrinho'] = carrinho
    request.session.modified = True

def addcarrinho_dig(request):
    dig = get_object_or_404(DigitacaoDetalhes, nome='Digitação')  
    carrinho = request.session.get('carrinho', {})

    # Use o nome do curso como identificador no carrinho
    dig_key = f'dig-{dig.nome}'

    # Verifica se o curso já foi adicionado ao carrinho
    if dig_key not in carrinho:
        carrinho[dig_key] = 1  # Adiciona ao carrinho com quantidade 1
    
    request.session['carrinho'] = carrinho
    request.session.modified = True

def AddCarrinho(request, id):
    adicionar_ao_carrinho(request, id)
    return redirect('pedido:continuarcarrinho', id=id)

def AddCarrinhoDig(request):
    addcarrinho_dig(request)
    return redirect('pedido:continuarcarrinhodig')


def Carrinho(request):
    carrinho = request.session.get('carrinho', {})

    # IDs numéricos para cursos normais
    curso_ids = [int(k) for k in carrinho.keys() if not k.startswith('dig-')]
    cursos = Curso.objects.filter(id__in=curso_ids)

    # Strings para cursos de digitação
    digitacao_key = [k for k in carrinho.keys() if k.startswith('dig-')]
    digitacao_curso = None
    if digitacao_key:
        nome_curso_dig = digitacao_key[0].split('-')[1]
        digitacao_curso = DigitacaoDetalhes.objects.filter(nome=nome_curso_dig).first()

    # Calcular o total dos valores
    total = sum(curso.preco for curso in cursos)
    if digitacao_curso:
        total += digitacao_curso.valor

    total_itens = sum(carrinho.values())
    

    dados = {
        'cursos': cursos,
        'digitacao_curso': digitacao_curso,
        'carrinho': carrinho,
        'total_itens': total_itens,
        'total': total,
    }
    return render(request, 'pedido.html', dados)



def ContinuarCarrinho(request, id):
    curso = get_object_or_404(Curso, id=id)
    carrinho = request.session.get('carrinho', {})
    
    if str(id) not in carrinho:
        carrinho[str(id)] = 1
        request.session['carrinho'] = carrinho
        request.session.modified = True
        
    cursos = Curso.objects.filter(id__in=[int(k) for k in carrinho.keys() if not k.startswith('dig-')])
    
    dados = {
        'curso': curso,
        'cursos': cursos,
        'carrinho': carrinho,
    }
    return render(request, 'continuarcarrinho.html', dados)


def ContinuarCarrinhoDig(request):
    # Substitua 'Curso de Digitação' pelo nome do curso no banco de dados
    dig = get_object_or_404(DigitacaoDetalhes, nome='Digitação')
    carrinho = request.session.get('carrinho', {})

    dig_key = f'dig-{dig.nome}'

    if dig_key not in carrinho:
        carrinho[dig_key] = 1
        request.session['carrinho'] = carrinho
        request.session.modified = True
    
    dados = {
        'dig': dig,
        'carrinho': carrinho,
    }
    return render(request, 'continuarcarrinhodig.html', dados)

def RemoverCarrinho(request, id):
    carrinho = request.session.get('carrinho', {})
    if str(id) in carrinho:
        del carrinho[str(id)]  # Remove o item do carrinho

    request.session['carrinho'] = carrinho
    return redirect('pedido:carrinho')  # Redireciona de volta para a página do carrinho

def RemoverCarrinhoDig(request):
    carrinho = request.session.get('carrinho', {})
    dig_key = None
    for key in carrinho.keys():
        if key.startswith('dig-'):
            dig_key = key
            break
        
    if dig_key:
        del carrinho[dig_key]  # Remove o curso de digitação do carrinho
    
    request.session['carrinho'] = carrinho
    return redirect('pedido:carrinho')  # Redireciona de volta para a página do carrinho

def Resumo(request):
    carrinho = request.session.get('carrinho', {})

    # Filtrar cursos normais (não digitação)
    cursos = Curso.objects.filter(id__in=[int(k) for k in carrinho.keys() if not k.startswith('dig-')])
    
    # Filtrar curso de digitação
    digitacao_key = [k for k in carrinho.keys() if k.startswith('dig-')]
    
    # Verifica se existe um curso de digitação no carrinho e recupera o primeiro
    digitacao_curso = None
    if digitacao_key:
        nome_curso_dig = digitacao_key[0].split('-')[1]  # Extrai o nome do curso de digitação
        digitacao_curso = DigitacaoDetalhes.objects.filter(nome=nome_curso_dig).first()

    # Calcular o total dos valores
    total = sum(curso.preco for curso in cursos)
    if digitacao_curso:
        total += digitacao_curso.valor

    total_itens = sum(carrinho.values())

    dados = {
        'cursos': cursos,
        'digitacao_curso': digitacao_curso,
        'carrinho': carrinho,
        'total_itens': total_itens,
        'total': total,
    }
    return render(request, 'resumo.html', dados)



