from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Curso,Turma
from django.shortcuts import render, get_object_or_404


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

def portal_professor(request):
    return render(request, 'instsoli/pages/portal_professor/portal_professor.html')

def gerenciar_turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'instsoli/pages/portal_professor/gerenciar_turmas.html', context={
        'turmas':turmas
    })

def criar_turma(request):
    return render(request,'instsoli/pages/portal_professor/criar_turma.html')


