from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso,Turma 
from usuario.models import InformacoesPessoais
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

def is_admin(user):
    if not user.is_superuser:
        return False 
    return True

def home(request):
    return render(request, 'instsoli/pages/home.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'instsoli/pages/cursos/cursos.html', context={
        'cursos':cursos
    })

def detalhe_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'instsoli/pages/cursos/cursos_detalhes.html', context={
        'curso': curso
    })

@login_required(login_url='usuario:login')
@user_passes_test(is_admin, login_url='instsoli:home')
def portal_professor(request):
    return render(request, 'instsoli/pages/portal_professor/portal_professor.html')

@login_required(login_url='usuario:login')
@user_passes_test(is_admin, login_url='instsoli:home')
def gerenciar_turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'instsoli/pages/portal_professor/gerenciar_turmas.html', context={
        'turmas':turmas
    })

@login_required(login_url='usuario:login')
@user_passes_test(is_admin, login_url='instsoli:home')
def criar_turma(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        curso_id = request.POST.get('curso')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        alunos_ids = request.POST.getlist('alunos')

        curso = Curso.objects.get(id=curso_id)
        turma = Turma.objects.create(
            nome=nome,
            curso=curso,
            data_inicio=data_inicio,
            data_fim=data_fim
        )

        if alunos_ids:
            turma.alunos.set(alunos_ids)

        return redirect('instsoli:gerenciar_turmas')

    cursos = Curso.objects.all()
    alunos = InformacoesPessoais.objects.all()

    return render(request, 'instsoli/pages/portal_professor/criar_turma.html', {
        'cursos': cursos,
        'alunos': alunos,
    })

def editar_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    cursos = Curso.objects.all()
    alunos = InformacoesPessoais.objects.all()

    if request.method == 'POST':
        turma.nome = request.POST.get('nome')
        turma.curso_id = request.POST.get('curso')
        turma.data_inicio = request.POST.get('data_inicio')
        turma.data_fim = request.POST.get('data_fim')
        
        turma.save()

        alunos_ids = request.POST.getlist('alunos')
        turma.alunos.set(alunos_ids)

        return redirect('instsoli:gerenciar_turmas')

    return render(request, 'instsoli/pages/portal_professor/editar_turma.html', context={
        'turma': turma,
        'cursos': cursos,
        'alunos': alunos,
    })

@login_required(login_url='usuario:login')
@user_passes_test(is_admin)
def excluir_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    turma.delete()
    messages.success(request, 'Turma excluída com sucesso!')
    return redirect('instsoli:gerenciar_turmas')
