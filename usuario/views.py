from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import InformacoesPessoais
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.method == "GET":
        if 'form_data' not in request.session:
            request.session['form_data'] = {}
        return render(request, "usuario/pages/register.html", {'form_data': request.session['form_data']})
    
    form_data = {
        'username': request.POST.get("username"),
        'email': request.POST.get("email"),
        'first_name': request.POST.get("first_name"),
        'last_name': request.POST.get("last_name"),
        'cpf': request.POST.get("CPF"),
        'telefone': request.POST.get("telefone"),
        'data_nascimento': request.POST.get("data_nascimento"),
        'genero': request.POST.get("genero"),
        'cep': request.POST.get("CEP"),
        'endereco': request.POST.get("endereco"),
        'numero': request.POST.get("numero"),
        'bairro': request.POST.get("bairro"),
        'estado': request.POST.get("estado"),
        'cidade': request.POST.get("cidade"),
        'escolaridade': request.POST.get("escolaridade"),
        'escola': request.POST.get("escola"),
        'turno': request.POST.get("turno"),
        'curso': request.POST.get("curso"),
        'pergunta': request.POST.get("pergunta"),
        'resposta': request.POST.get("resposta"),
    }
    request.session['form_data'] = form_data
    
    # Validação das senhas
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")
    
    if password != confirm_password:
        messages.error(request, "As senhas não coincidem.")
        return render(request, "usuario/pages/register.html", {'form_data': form_data})
    
    # Validação de usuário existente
    if User.objects.filter(username=form_data['username']).exists():
        messages.error(request, "Este nome de usuário já está em uso.")
        return render(request, "usuario/pages/register.html", {'form_data': form_data})
    
    # Validação de email existente
    if User.objects.filter(email=form_data['email']).exists():
        messages.error(request, "Este email já está cadastrado.")
        return render(request, "usuario/pages/register.html", {'form_data': form_data})
    
    try:
        user = User.objects.create_user(
            username=form_data['username'],
            email=form_data['email'],
            password=password,
            first_name=form_data['first_name'],
            last_name=form_data['last_name']
        )

        InformacoesPessoais.objects.create(
            user=user,
            cpf=form_data['cpf'],
            telefone=form_data['telefone'],
            data_nascimento=form_data['data_nascimento'],
            genero=form_data['genero'],
            cep=form_data['cep'],
            endereco=form_data['endereco'],
            numero=form_data['numero'],
            bairro=form_data['bairro'],
            estado=form_data['estado'],
            cidade=form_data['cidade'],
            escolaridade=form_data['escolaridade'],
            escola=form_data['escola'],
            turno=form_data['turno'],
            curso=form_data['curso'],
        )
        
        del request.session['form_data']
        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect("usuario:login")
        
    except Exception as e:
        messages.error(request, f"Ocorreu um erro durante o cadastro: {str(e)}")
        return render(request, "usuario/pages/register.html", {'form_data': form_data})

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