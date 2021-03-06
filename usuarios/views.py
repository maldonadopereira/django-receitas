from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from receitas.models import Receita
from django.contrib import messages


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')

        if senhas_diferentes(password, password2):
            messages.error(request, 'As senhas não são iguais!!')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Esse usuário já está cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Esse usuário já está cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Usuário cadastrado om sucesso!')
        return redirect('login')
    else:

        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if not email.strip() or not password.strip():
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=password)

            if user is not None:
                auth.login(request, user)
                print(f'Olá, {nome} você logou com sucesso!!')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')


#@login_required
def dashboard(request):
    if request.user.is_authenticated:
            id = request.user.id
            receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)
            dados = {
                'receitas': receitas
            }
            return render(request, 'usuarios/dashboard.html', dados)

    else:
        return redirect('usuarios/index.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def campo_vazio(campo):
    return not campo.strip()


def senhas_diferentes(password, password2):
    return password != password2