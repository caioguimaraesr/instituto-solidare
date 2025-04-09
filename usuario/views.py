from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.method == "GET":
        return render(request, 'usuario/pages/register.html')
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    
    admin = request.POST.get('admin')
    usuario = request.POST.get('usuario')
    admin_password = request.POST.get('admin_password')

    if password != confirm_password:
        messages.error(request, 'As senhas não estão iguais.')
    
    user = User.objects.filter(username=username)

    if user:
        messages.error(request, 'Usuário já existente.')
        return redirect('usuario:register')

    if admin:
        if admin_password != 'senha':
            messages.error(request, 'Senha de administrador incorreta.')
            return redirect('usuario:register')

        user = User.objects.create_superuser(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=password
    )
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso.')
        return redirect('usuario:login')
    
    elif usuario:
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        ) 
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso.')
        return redirect('usuario:login')
    
    messages.error(request, 'Por favor, selecione um tipo de usuário.')
    return redirect('usuario:register')

def login_view(request):
    if request.method == "GET":
        return render(request, 'usuario/pages/login.html')
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return redirect('instsoli:home')
    else:
        messages.error(request, 'Dados inválidos.')
        return redirect('usuario:login')

@login_required(login_url='usuario:login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('usuario:login')