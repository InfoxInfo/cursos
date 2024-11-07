from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, CriarUsuarioForm

def criar_usuario_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        criar_usuario_form = CriarUsuarioForm(request.POST)
        
        if 'login' in request.POST and login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('pedido:resumo')
        elif 'criar_conta' in request.POST and criar_usuario_form.is_valid():
            criar_usuario_form.save()
            user = authenticate(username=criar_usuario_form.cleaned_data['username'], password=criar_usuario_form.cleaned_data['password1'])
            login(request, user)
            return redirect('pedido:resumo')
    else:
        login_form = LoginForm()
        criar_usuario_form = CriarUsuarioForm()

    context = {
        'login_form': login_form,
        'criar_usuario_form': criar_usuario_form,
    }
    
    return render(request, 'criar.html', context)
